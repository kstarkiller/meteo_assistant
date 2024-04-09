import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
import time

from functions.weather_class import Base

from ..config import DATABASE, USER, PASSWORD, PORT, DB_HOST

def connect_to_database():
    # Create the engine
    while True:
        try:
            engine = create_engine(f'postgresql://{USER}:{PASSWORD}@{DB_HOST}:{PORT}/{DATABASE}')
            break
        except OperationalError:
            print("Database not ready yet, waiting and retrying...")
            time.sleep(1)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    return session

def create_table(session):
    # Create the table if it doesn't exist
    Base.metadata.create_all(session.get_bind())
