import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://localhost/mammoth') 
engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
