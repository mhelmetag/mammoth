import os
import re

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://localhost/mammoth')

# Heroku uses postgres:// but sqlalchemy wants postgresql://
CORRECTED_DATABASE_URL = re.sub('postgres:', 'postgresql:', DATABASE_URL)
engine = create_engine(CORRECTED_DATABASE_URL, connect_args={
                       "options": "-c timezone=utc"})

Session = sessionmaker(bind=engine)
