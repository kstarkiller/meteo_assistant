import sys
import os
from sqlalchemy import create_engine, Column, Integer, String, Float, BigInteger, JSON, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir, os.path.pardir)))
from hidden import DATABASE, USER, PASSWORD, HOST, PORT

Base = declarative_base()

class MeteoFrance(Base):
    __tablename__ = 'meteo_france'

    id = Column(Integer, primary_key=True)
    city = Column(String(100))
    latitude = Column(Float)
    longitude = Column(Float)
    date = Column(DateTime)
    tmin = Column(Float)
    tmax = Column(Float)
    hmin = Column(Integer)
    hmax = Column(Integer)
    precipitation = Column(Float)
    sunrise = Column(BigInteger)
    sunset = Column(BigInteger)
    weather_desc = Column(String(100))
    weather_icon = Column(String(100))
    rain_status = Column(String(100))
    readable_warnings = Column(JSON)

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
