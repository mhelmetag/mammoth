from app.models.base import Base

from sqlalchemy import Column, Integer, JSON


class LatestUpdate(Base):
    __tablename__ = 'latest_updates'

    id = Column(Integer, primary_key=True)
    updates = Column(JSON, nullable=False)
