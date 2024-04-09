import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
import time

from functions.weather_class import MeteoFrance

# Get the environment variables
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
DB_HOST = os.getenv('DB_HOST')
PORT = os.getenv('PORT')
DATABASE = os.getenv('DATABASE')

# Check if each environment variables are set
if not USER :
    raise ValueError("USER environment variable not set")
elif not PASSWORD :
    raise ValueError("PASSWORD environment variable not set")
elif not DB_HOST :
    raise ValueError("DB_HOST environment variable not set")
elif not PORT :
    raise ValueError("PORT environment variable not set")
elif not DATABASE :
    raise ValueError("DATABASE environment variable not set")


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
    MeteoFrance.metadata.create_all(session.get_bind())
