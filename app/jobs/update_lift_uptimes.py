from dateutil.tz.tz import gettz
from app.db.session import Session
from app.models.lift import Lift
from app.models.latest_update import LatestUpdate
from app.shared.uptime_service import UptimeService

import os
from datetime import datetime

SEASON = os.getenv('SEASON', 'Winter')
# I wanted the day of week for yesterday to be easier to calculate
# so that 0 - 1 would be 6 (days_of_week[-1]) instead of -1
# by using array wrapping
DAYS_OF_WEEK = list(range(0, 7))


def main():
    # Run daily at 5AM UTC with cron
    session = Session()

    try:
        seasonal_lifts = session.query(
            Lift.name).filter(Lift.season == SEASON).all()
        seasonal_lift_names = list(map(lambda lift: lift.name, seasonal_lifts))

        time_now_pt = datetime.now(tz=gettz('America/Los_Angeles'))
        day_of_week_yesterday = DAYS_OF_WEEK[time_now_pt.weekday - 1]
        yesterday_start = datetime(
            time_now_pt.year, time_now_pt.month, time_now_pt.day - 1)
        yesterday_end = datetime(
            time_now_pt.year, time_now_pt.month, time_now_pt.day)
        latest_updates = session.query(LatestUpdate).filter(
            Lift.last_updated.between(yesterday_start, yesterday_end)).all()

        uptime_service = UptimeService(
            seasonal_lift_names, day_of_week_yesterday, latest_updates)
        uptimes = uptime_service.calculate_uptimes()

        for lift_name in uptimes:
            uptime = uptimes[lift_name]
            lift = session.query(Lift).filter(
                Lift.season == SEASON, Lift.name == lift_name).first()

            lift.uptime = uptime

            session.commit()

    finally:
        session.close()


main()
