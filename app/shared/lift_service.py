import os
from datetime import datetime
from dateutil.parser import parse
from dateutil.tz import gettz

from requests import get
from bs4 import BeautifulSoup


class LiftService:
    def __init__(self):
        self.season = os.getenv('SEASON')

    def fetch_lifts(self):
        url = self._status_url()
        response = get(url)
        json = response.json()
        html = json['data']
        soup = BeautifulSoup(html, 'html.parser')
        rows = soup.find('tbody').findAll('tr')

        lifts = []
        for row in rows:
            name_element = row.find('td', {'class': 'lift-description'})
            status_element = row.find('td', {'class': 'lift-status-icon'})

            if name_element and status_element:
                name = name_element.getText()
                status = self._translate_status(status_element['class'][1])
                kind = self._translate_kind(
                    row.find('td', {'class': 'lift-chair-icon'})['class'][1])
                season = self.season
                last_updated = self._last_updated(
                    row.find('td', {'class': 'lift-last-update'}).find('span').getText())

                lift = {
                    "name": name,
                    "status": status,
                    "kind": kind,
                    "season": season,
                    "last_updated": last_updated
                }

                lifts.append(lift)

        return lifts

    def _status_url(self):
        if self.season == 'Winter':
            return os.getenv('MAMMOTH_WINTER_LIFT_STATUS_URL')
        else:
            return os.getenv('MAMMOTH_SUMMER_LIFT_STATUS_URL')

    def _translate_status(self, status):
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

    def _translate_kind(self, kind):
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

    def _last_updated(self, last_updated_raw):
        if last_updated_raw != 'N/A':
            last_updated_pst = f"{last_updated_raw} PST"
            return parse(last_updated_pst, tzinfos={
                'PST': gettz('America/Los_Angeles')})
        else:
            return datetime.utcnow()
