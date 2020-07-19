from app.db.session import Session
from app.models.lift import Lift

from app.shared.lift import status_url, translate_kind, translate_status

import os
from datetime import datetime

from dateutil.parser import parse
from dateutil.tz import gettz
from requests import get
from bs4 import BeautifulSoup


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

        for row in rows:
            name_element = row.find('td', {'class': 'lift-description'})
            status_element = row.find('td', {'class': 'lift-status-icon'})

            if name_element and status_element:
                name = name_element.getText()
                status = translate_status(status_element['class'][1])
                kind = translate_kind(
                    row.find('td', {'class': 'lift-chair-icon'})['class'][1])
                last_updated_raw = row.find(
                    'td', {'class': 'lift-last-update'}).find('span').getText()
                last_updated = datetime.utcnow()

                if last_updated_raw != 'N/A':
                    last_updated_pst = f"{last_updated_raw} PST"
                    last_updated = parse(last_updated_pst, tzinfos={
                        'PST': gettz('America/Los_Angeles')})

                lift = Lift(
                    name=name,
                    status=status,
                    kind=kind,
                    season=season,
                    last_updated=last_updated
                )

                session.add(lift)
                session.commit()
    finally:
        session.close()


main()
