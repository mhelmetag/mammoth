from app.models.base import Base

from dateutil.tz import gettz
from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime


class Lift(Base):
    __tablename__ = 'lifts'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    status = Column(String, nullable=False)
    kind = Column(String, nullable=False)
    last_updated = Column(DateTime, nullable=False)

    def _for_html(self):
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status,
            'kind': self.kind,
            'last_updated': self._last_updated_for_html()
        }

    def _for_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status,
            'kind': self.kind,
            'last_updated': self._last_updated_for_json()
        }

    def _last_updated_for_html(self):
        last_updated = self.last_updated
        time_since_last_updated = datetime.now() - last_updated

        if time_since_last_updated.days >= 1:
            return 'A long time ago'
        else:
            return last_updated.replace(tzinfo=gettz('UTC')).astimezone(
                tz=gettz('America/Los_Angeles')).strftime('%-I:%M %p %Z')

    def _last_updated_for_json(self):
        return self.last_updated.replace(tzinfo=gettz('UTC')).isoformat()
