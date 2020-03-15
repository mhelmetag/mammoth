import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://localhost/mammoth') 
engine = create_engine(DATABASE_URL, connect_args={"options": "-c timezone=utc"})

Session = sessionmaker(bind=engine)
