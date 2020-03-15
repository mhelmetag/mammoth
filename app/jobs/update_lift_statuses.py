from app.db.session import Session
from app.models.lift import Lift
from app.shared.firebase import init_firebase_admin

import os

from dateutil.parser import parse
from dateutil.tz import gettz
from requests import get
from bs4 import BeautifulSoup
import firebase_admin
from firebase_admin import messaging

init_firebase_admin()


def main():
    session = Session()

    response = get(os.getenv('MAMMOTH_STATUS_URL'))
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

            lift = session.query(Lift).filter(Lift.name == name).first()

            if lift and lift.status != status and last_updated_raw != 'N/A':
                last_updated_pst = f"{last_updated_raw} PST"
                last_updated = parse(last_updated_pst, tzinfos={
                    'PST': gettz('America/Los_Angeles')})

                lift.status = status
                lift.last_updated = last_updated
                session.commit()

                updated.append(lift)

    if any(updated):
        notification = messaging.Notification(
            image=f"{os.getenv('BASE_URL')}/static/icon.png",
            title='New Lift Updates from Mammoth',
            body=f'{len(updated)} Lift(s) has/have updated status(es)'
        )
        message = messaging.Message(
            topic='updates',
            notification=notification
        )

        messaging.send(message)

    session.close()


def translate_status(status):
    if status == 'open':
        return 'Open'
    elif status == 'sceniconly':
        return 'For Scenic Rides Only'
    elif status == 'within30':
        return '30 Minutes or Less'
    elif status == 'expected':
        return 'Expected'
    elif status == 'weatherhold':
        return 'Hold - Weather'
    elif status == 'maintenancehold':
        return 'Hold - Maintenance'
    elif status == 'closed':
        return 'Closed'
    else:
        return 'Unknown'


main()
