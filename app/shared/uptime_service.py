from app.models.lift import Lift

from datetime import datetime
import os


# Lift schedules follow a Monday - Sunday order
# with open and close times in 24H style
# in UTC

SUMMER_LIFT_SCHEDULES = {
    'Panorama Lower': [
        [9, 17],
        [9, 17],
        [9, 17],
        [9, 17],
        [9, 17],
        [9, 17],
        [9, 17]
    ],
    'Panorama Upper': [
        [9, 17],
        [9, 17],
        [9, 17],
        [9, 17],
        [9, 17],
        [9, 17],
        [9, 17]
    ],
    'Discovery Express 11': [
        [9, 17],
        [9, 17],
        [9, 17],
        [9, 17],
        [9, 17],
        [9, 17],
        [9, 17]
    ],
    'Canyon Express 16': [
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [10, 18],
        [10, 18],
        [10, 18]
    ],
    'Stump Alley Express 2': [
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [10, 18],
        [10, 18],
        [10, 18]
    ]
}

# TODO: Will have to figure this out when they post it
WINTER_LIFT_SCHEDULES = {}


class UptimeService:
    def __init__(self, seasonal_lifts: list[str], day_of_week: int, latest_updates: list):
        self.lift_schedules = self._lift_schedules()
        self.seasonal_lifts = seasonal_lifts
        self.day_of_week = day_of_week
        self.latest_updates = latest_updates

    def calculate_uptimes(self):
        uptimes = {}

        for seasonal_lift in self.seasonal_lifts:
            uptimes[seasonal_lift] = 0

        grouped_updates = self._group_updates()

        for lift_name in grouped_updates:
            uptime = self._calculate_uptime(lift_name, grouped_updates)

            if uptime:
                uptimes[lift_name] = uptime

        return uptimes

    def _calculate_uptime(self, lift_name, grouped_updates):
        lift_schedule = self.lift_schedules[lift_name]
        lift_updates = grouped_updates[lift_name]

        if lift_schedule:
            open_hour, close_hour = lift_schedule[self.day_of_week]

            # Uptime is 0 if the lift isn't open
            if open_hour == 0:
                next

            scheduled_minutes_open = (close_hour - open_hour) * 60
            minutes_closed = self._calculate_minutes_closed(
                open_hour, close_hour, lift_updates)

            return round(((scheduled_minutes_open - minutes_closed) / scheduled_minutes_open) * 100)

    def _calculate_minutes_closed(self, _, close_hour, updates):
        minutes_closed = 0
        open = False
        last_closed = None

        for update in updates:
            created_at = datetime.fromisoformat(update['created_at'])

            if update['to'] in Lift.OPEN_STATUSES:
                if not open and last_closed:
                    difference_minutes = (
                        created_at - last_closed).seconds / 60
                    minutes_closed += difference_minutes
                    last_closed = None

                open = True
            else:
                open = False
                last_closed = created_at

        # TODO: Should consider late opening but... that's next

        if last_closed.hour < close_hour:
            close_time = datetime(
                last_closed.year, last_closed.month, last_closed.day, close_hour)
            difference_minutes = (close_time - last_closed).seconds / 60
            minutes_closed += difference_minutes

        return minutes_closed

    def _group_updates(self):
        # If updates were stored flat, this would be easier

        grouped_updates = {}

        for latest_update in self.latest_updates:
            for update in latest_update['updates']:
                lift_name = update['name']
                u = {
                    'from': update['from'],
                    'to': update['to'],
                    'created_at': latest_update['created_at']
                }

                if type(grouped_updates.get(lift_name)) == list:
                    grouped_updates[lift_name].append(u)
                else:
                    grouped_updates[lift_name] = [u]

        return grouped_updates

    def _lift_schedules(self):
        if os.getenv('SEASON', 'Winter') == 'Winter':
            return WINTER_LIFT_SCHEDULES
        else:
            return SUMMER_LIFT_SCHEDULES
