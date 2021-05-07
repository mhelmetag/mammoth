from app.models.base import Base

from dateutil.tz import gettz

from sqlalchemy import Column, Integer, DateTime, JSON


class LatestUpdate(Base):
    __tablename__ = 'latest_updates'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, nullable=False)
    updates = Column(JSON, nullable=False)

    def for_html(self):
        return {
            'created_at': self._created_at_for_html(),
            'updates': self.updates
        }

    def for_json(self):
        return {
            'created_at': self._created_at_for_json(),
            'updates': self.updates
        }

    def _created_at_for_html(self):
        return self.created_at.replace(tzinfo=gettz('UTC')).astimezone(
            tz=gettz('America/Los_Angeles')).strftime('%-I:%M %p %Z')

    def _created_at_for_json(self):
        self.created_at.replace(tzinfo=gettz('UTC')).isoformat()
