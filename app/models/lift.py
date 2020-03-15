from app.models.base import Base

from dateutil.tz import gettz

from sqlalchemy import Column, Integer, String, DateTime

class Lift(Base):
    __tablename__ = 'lifts'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    status = Column(String, nullable=False)
    kind = Column(String, nullable=False)
    last_updated = Column(DateTime, nullable=False)

    def _asdict(self):
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status,
            'kind': self.kind,
            'last_updated': self.last_updated.replace(tzinfo=gettz('UTC')).astimezone(tz=gettz('America/Los_Angeles')).strftime('%-I:%M %p %Z')
        }
