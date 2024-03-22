from datetime import datetime, timedelta
from sqlalchemy.sql.expression import extract
from sqlalchemy import delete
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime

Base = declarative_base()


class MeteoFrance(Base):
    __tablename__ = 'french_cities_weather'

    id = Column(Integer, primary_key=True)
    city = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    date = Column(DateTime)
    temperature = Column(Float)
    humidity = Column(Float)
    rain = Column(String)
    snow = Column(String)
    clouds = Column(Integer)
    wind = Column(String)
    weather_desc = Column(String)
    weather_icon = Column(String)
    readable_warnings = Column(String)
    add_date = Column(DateTime)

def delete_former_data(session):
    # Get the current datetime
    now = datetime.now()

    # Construct the SQLAlchemy delete query
    query = delete(MeteoFrance).where(MeteoFrance.date < now - timedelta(days=1))

    # Execute the delete query
    session.execute(query)

    # Commit the transaction
    session.commit()
