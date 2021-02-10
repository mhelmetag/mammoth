from app.shared.notification_service import NotificationService
from app.db.session import Session
from app.models.lift import Lift
from app.shared.lift_service import LiftService
from app.shared.firebase import init_firebase_admin

import os

SEASON = os.getenv('SEASON', 'Winter')
ENV = os.getenv('APP_ENV', 'development')

init_firebase_admin()


def main():
    session = Session()

    try:
        lift_service = LiftService()
        lifts = lift_service.fetch_lifts()

        updated = []
        for lift in lifts:
            stored_lift = session.query(Lift).filter(
                Lift.season.like(SEASON), Lift.name.like(lift['name'])).first()

            if stored_lift and stored_lift.status != lift['status']:
                stored_lift.status = lift['status']
                stored_lift.last_updated = lift['last_updated']

                session.commit()

                updated.append(lift)

        if any(updated):
            notification_service = NotificationService(len(updated))
            notification_service.send_notifications()

    finally:
        session.close()


main()
