from app.shared.notification_service import NotificationService
from app.db.session import Session
from app.models.lift import Lift
from app.shared.lift_service import LiftService
from app.models.latest_update import LatestUpdate
from app.shared.firebase import init_firebase_admin

import os
from datetime import datetime

SEASON = os.getenv('SEASON', 'Winter')
ENV = os.getenv('APP_ENV', 'development')

init_firebase_admin()


def main():
    session = Session()

    try:
        lift_service = LiftService()
        lifts = lift_service.fetch_lifts()

        updates = []
        for lift in lifts:
            stored_lift = session.query(Lift).filter(
                Lift.season.like(SEASON), Lift.name.like(lift['name'])).first()

            if stored_lift and stored_lift.status != lift['status']:
                update = {
                    'name': stored_lift.name,
                    'from': stored_lift.status,
                    'to': lift['status']
                }

                stored_lift.status = lift['status']
                stored_lift.last_updated = lift['last_updated']

                session.commit()

                updates.append(update)

        if any(updates):
            current_time = datetime.utcnow()
            latest_update = LatestUpdate(
                created_at=current_time, updates=updates, season=SEASON)

            session.add(latest_update)

            session.commit()

            notification_service = NotificationService(len(updates))
            notification_service.send_notifications()

    finally:
        session.close()


main()
