import sys
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir, os.path.pardir)))
from hidden import DATABASE, USER, PASSWORD, HOST, PORT

from functions.weather_class import Base

def connect_to_database():
    # Create the engine
    engine = create_engine(f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}')

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    return session

def create_table(session):
    # Create the table if it doesn't exist
    Base.metadata.create_all(session.get_bind())
