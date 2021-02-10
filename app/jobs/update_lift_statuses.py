from app.db.session import Session
from app.models.lift import Lift
from app.shared.lift_service import LiftService
from app.shared.firebase import init_firebase_admin

import os

from firebase_admin import messaging

SEASON = os.getenv('SEASON', 'Winter')
ENV = os.getenv('APP_ENV', 'development')

init_firebase_admin()


def _notification_body(updated):
    if len(updated) == 1:
        return f'1 lift has an updated status'
    else:
        return f'{len(updated)} lifts have updated statuses'


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
            title = 'New Lift Updates from Mammoth'
            body = _notification_body(updated)
            notification = messaging.Notification(
                title=title,
                body=body
            )
            message = messaging.Message(
                topic='updates',
                notification=notification
            )

            messaging.send(message)

    finally:
        session.close()


main()
