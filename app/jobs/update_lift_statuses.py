from app.db.session import Session
from app.models.lift import Lift
from app.shared.firebase import init_firebase_admin

from app.shared.lift import status_url, translate_status

import os
from datetime import datetime

from dateutil.parser import parse
from dateutil.tz import gettz
from requests import get
from bs4 import BeautifulSoup
from firebase_admin import messaging

init_firebase_admin()


def main():
    session = Session()

    try:
        season = os.getenv('SEASON')
        url = status_url(season)
        response = get(url)
        json = response.json()
        html = json['data']
        soup = BeautifulSoup(html, 'html.parser')
        rows = soup.find('tbody').findAll('tr')

        updated = []
        for row in rows:
            name_element = row.find('td', {'class': 'lift-description'})
            status_element = row.find('td', {'class': 'lift-status-icon'})

            if name_element and status_element:
                name = name_element.getText()
                status = translate_status(status_element['class'][1])
                last_updated_raw = row.find(
                    'td', {'class': 'lift-last-update'}).find('span').getText()

                lift = session.query(Lift).filter(
                    Lift.season.like(season), Lift.name.like(name)).first()

                if lift and lift.status != status:
                    last_updated = datetime.utcnow()

                    if last_updated_raw != 'N/A':
                        last_updated_pst = f"{last_updated_raw} PST"
                        last_updated = parse(last_updated_pst, tzinfos={
                            'PST': gettz('America/Los_Angeles')})

                    lift.status = status
                    lift.last_updated = last_updated
                    session.commit()

                    updated.append(lift)

        if any(updated):
            title = 'New Lift Updates from Mammoth'

            body = ""
            if len(updated) == 1:
                body = f'1 Lift has an updated status'
            else:
                body = f'{len(updated)} Lifts have updated statuses'

            webpush_notification = messaging.WebpushNotification(
                title=title,
                body=body,
                icon=f"{os.getenv('BASE_URL')}/static/icon.png",
                badge=f"{os.getenv('BASE_URL')}/static/icon.png",
                renotify=True
            )

            link = ""
            if os.getenv('APP_ENV', 'development') == 'production':
                link = os.getenv('BASE_URL')

            webpush_fcm_options = messaging.WebpushFCMOptions(
                link=link
            )
            webpush_config = messaging.WebpushConfig(
                notification=webpush_notification,
                fcm_options=webpush_fcm_options
            )
            notification = messaging.Notification(
                title=title,
                body=body
            )
            message = messaging.Message(
                topic='updates',
                notification=notification,
                webpush=webpush_config
            )

            messaging.send(message)

    finally:
        session.close()


main()
