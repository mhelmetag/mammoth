from app.models.base import Base

from dateutil.tz import gettz

from sqlalchemy import Column, Integer, DateTime, JSON


class LatestUpdate(Base):
    __tablename__ = 'latest_updates'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, nullable=False)
    updates = Column(JSON, nullable=False)

    def for_json(self):
        return {
            'created_at': self.created_at.replace(tzinfo=gettz('UTC')).isoformat(),
            'updates': self.updates
        }
