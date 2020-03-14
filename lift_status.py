from requests import get
from bs4 import BeautifulSoup

def main():
  response = get('https://www.mammothmountain.com/mvc/lifttraildata/getliftdata?resort=1&view=_mmsa_lift_status')
  json = response.json()
  html = json['data']
  soup = BeautifulSoup(html, 'html.parser')
  rows = soup.find('tbody').findAll('tr')
  lifts = []

  for row in rows:
    lift_name = row.find('td', {'class': 'lift-description'})
    lift_status = row.find('td', {'class': 'lift-status-icon'})

    if lift_name and lift_status:
      lifts.append(
        {
          'name': lift_name.getText(),
          'status': translate_status(lift_status['class'][1]),
          'type': 'Chairlift',
          'last_updated_at': row.find('td', {'class': 'lift-last-update'}).find('span').getText()
        }
      )

  for lift in lifts:
    print(
      f"""
      Lift: {lift['name']}
      Status: {lift['status']}
      Type: {lift['type']}
      Last Updated At: {lift['last_updated_at']}
      """
    )

def translate_status(class_status):
  if class_status == 'open':
    return 'Open'
  elif class_status == 'sceniconly':
    return 'For Scenic Rides Only'
  elif class_status == 'within30':
    return '30 Minutes or Less'
  elif class_status == 'expected':
    return 'Expected'
  elif class_status == 'weatherhold':
    return 'Hold - Weather'
  elif class_status == 'maintenancehold':
    return 'Hold - Maintenance'
  elif class_status == 'closed':
    return 'Closed'
  else:
    return 'Unknown'

main()
