import os


def status_url(season):
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


def translate_kind(kind):
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
