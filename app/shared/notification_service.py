import os

from firebase_admin import messaging

APP_ENV = os.getenv('APP_ENV', 'development')
BASE_URL = os.getenv('BASE_URL', 'http://localhost:8000')
MESSAGE_TOPIC = 'updates'
NOTIFICATION_TITLE = 'New Lift Updates from Mammoth'


class NotificationService:
    def __init__(self, updated_count):
        self.updated_count = updated_count

    def send_notifications(self):
        message = self._message()

        messaging.send(message)

    def _message(self):
        if APP_ENV == 'development':
            return self._development_message()
        else:
            return self._production_message()

    def _development_message(self):
        notification = self._notification()
        message = messaging.Message(
            topic=MESSAGE_TOPIC,
            notification=notification
        )

        return message

    def _production_message(self):
        notification = self._notification()
        webpush_notification = messaging.WebpushNotification(
            icon=f'{BASE_URL}/static/icon.png'
        )
        webpush_fcm_options = messaging.WebpushFCMOptions(
            link=BASE_URL
        )
        webpush_config = messaging.WebpushConfig(
            notification=webpush_notification,
            fcm_options=webpush_fcm_options
        )
        message = messaging.Message(
            topic=MESSAGE_TOPIC,
            notification=notification,
            webpush=webpush_config
        )

        return message

    def _notification(self):
        body = self._notification_body()
        return messaging.Notification(
            title=NOTIFICATION_TITLE,
            body=body
        )

    def _notification_body(self):
        if self.updated_count == 1:
            return '1 lift has an updated status'
        else:
            return f'{self.updated_count} lifts have updated statuses'
