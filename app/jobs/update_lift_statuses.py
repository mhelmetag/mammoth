from app.db.session import Session
from app.models.lift import Lift
from app.shared.lift_service import LiftService
from app.shared.firebase import init_firebase_admin

import os

from firebase_admin import messaging

SEASON = os.getenv('SEASON')

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
            title = 'New Lift Updates from Mammoth'

            body = ''
            if len(updated) == 1:
                body = f'1 Lift has an updated status'
            else:
                body = f'{len(updated)} Lifts have updated statuses'

            webpush_notification = messaging.WebpushNotification(
                title=title,
                body=body,
                icon=f"{os.getenv('BASE_URL')}/static/icon.png",
                badge=f"{os.getenv('BASE_URL')}/static/icon.png",
                renotify=True
            )

            link = ''
            if os.getenv('APP_ENV', 'development') == 'production':
                link = os.getenv('BASE_URL')

            webpush_fcm_options = messaging.WebpushFCMOptions(
                link=link
            )
            webpush_config = messaging.WebpushConfig(
                notification=webpush_notification,
                fcm_options=webpush_fcm_options
            )
            notification = messaging.Notification(
                title=title,
                body=body
            )
            message = messaging.Message(
                topic='updates',
                notification=notification,
                webpush=webpush_config
            )

            messaging.send(message)

    finally:
        session.close()


main()
