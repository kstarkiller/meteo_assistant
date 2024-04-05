import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
import time

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir, os.path.pardir)))
# from hidden import DATABASE, USER, PASSWORD, HOST, PORT

from functions.weather_class import Base

# Import the required environment variables
DATABASE = os.getenv("DATABASE")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")

def connect_to_database():
    # Create the engine
    while True:
        try:
            engine = create_engine(f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}')
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
