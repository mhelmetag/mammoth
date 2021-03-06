from app.models.base import Base

from dateutil.tz import gettz
from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Index
from sqlalchemy.orm import validates


class Lift(Base):
    STATUSES = ['Open', 'For Scenic Rides Only', '30 Minutes or Less',
                'Expected', 'Hold - Weather', 'Hold - Maintenance', 'Closed', 'Unknown']
    KINDS = ['Double', 'Triple', 'Quad',
             'Six-pack', 'Gondola', 'Zipline', 'Unknown']
    SEASONS = ['Winter', 'Summer']

    __tablename__ = 'lifts'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    status = Column(String, nullable=False)
    kind = Column(String, nullable=False)
    season = Column(String, nullable=False)
    last_updated = Column(DateTime, nullable=False)

    @validates('status')
    def validate_status(self, key, status):
        if not status in self.STATUSES:
            raise ValueError("kind must be one of: ", self.STATUSES)
        else:
            return status

    @validates('kind')
    def validate_kind(self, key, kind):
        if not kind in self.KINDS:
            raise ValueError("kind must be one of: ", self.KINDS)
        else:
            return kind

    @validates('season')
    def validate_season(self, key, season):
        if not season in self.SEASONS:
            raise ValueError("kind must be one of: ", self.SEASONS)
        else:
            return season

    def _for_html(self):
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status,
            'kind': self.kind,
            'season': self.season,
            'last_updated': self._last_updated_for_html()
        }

    def _for_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status,
            'kind': self.kind,
            'season': self.season,
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
