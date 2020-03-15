from app.db.session import Session
from app.models.lift import Lift

from dateutil.parser import parse
from dateutil.tz import gettz

from requests import get
from bs4 import BeautifulSoup

def main():
  updated = []

  session = Session()

  response = get('https://www.mammothmountain.com/mvc/lifttraildata/getliftdata?resort=1&view=_mmsa_lift_status')
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
      last_updated_string = f"{row.find('td', {'class': 'lift-last-update'}).find('span').getText()} PST"
      last_updated = parse(last_updated_string, tzinfos={'PST': gettz('America/Los_Angeles')})

      lift = session.query(Lift).filter(Lift.name == name).one()

      if lift and lift.status != status:
        lift.status = status
        lift.last_updated = last_updated
        session.commit()

        updated.append(lift)

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