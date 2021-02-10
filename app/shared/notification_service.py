from firebase_admin import messaging

MESSAGE_TOPIC = 'updates'
NOTIFICATION_TITLE = 'New Lift Updates from Mammoth'


class NotificationService:
    def __init__(self, updated_count):
        self.updated_count = updated_count

    def send_notifications(self):
        body = self._notification_body()
        notification = messaging.Notification(
            title=NOTIFICATION_TITLE,
            body=body
        )
        message = messaging.Message(
            topic=MESSAGE_TOPIC,
            notification=notification
        )

        messaging.send(message)

    def _notification_body(self):
        if self.updated_count == 1:
            return '1 lift has an updated status'
        else:
            return f'{self.updated_count} lifts have updated statuses'
