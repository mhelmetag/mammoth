from app.models.base import Base

from sqlalchemy import Column, Integer, String

class Subscriber(Base):
    __tablename__ = 'subscribers'

    id = Column(Integer, primary_key=True)
    phone_number = Column(String, nullable=False, unique=True)

    def _asdict(self):
        return {
            'id': self.id,
            'phone_number': self.phone_number
        }
