from app.db.session import Session
from app.models.lift import Lift

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
        lift_status_url = get_lift_status_url(season)
        response = get(lift_status_url)
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
                kind = translate_chairlift_kind(
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


def get_lift_status_url(season):
    if season == 'Winter':
        return os.getenv('MAMMOTH_WINTER_LIFT_STATUS_URL')
    else:
        return os.getenv('MAMMOTH_SUMMER_LIFT_STATUS_URL')


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


def translate_chairlift_kind(kind):
    if kind == 'chair2':
        return 'Double'
    elif kind == 'chair3':
        return 'Triple'
    elif kind == 'chair4':
        return 'Quad'
    elif kind == 'chair6':
        return 'Six-pack'
    elif kind == 'gondola':
        return 'Gondola'
    elif kind == 'zipline':
        return 'Zipline'
    else:
        return 'Unknown'


main()
