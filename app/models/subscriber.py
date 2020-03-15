from app.models.base import Base

from sqlalchemy import Column, Integer, String


class Subscriber(Base):
    __tablename__ = 'subscribers'

    id = Column(Integer, primary_key=True)
    subscriber_id = Column(String, nullable=False, unique=True)

    def _asdict(self):
        return {
            'id': self.id,
            'subscriber_id': self.subscriber_id
        }
