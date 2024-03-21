import json
from datetime import datetime
from meteofrance_api.helpers import readeable_phenomenoms_dict
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class MeteoFrance(Base):
    __tablename__ = 'meteo_france'

    id = Column(Integer, primary_key=True)
    city = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    date = Column(DateTime)
    tmin = Column(Float)
    tmax = Column(Float)
    hmin = Column(Float)
    hmax = Column(Float)
    precipitation = Column(Float)
    sunrise = Column(DateTime)
    sunset = Column(DateTime)
    weather_desc = Column(String)
    weather_icon = Column(String)
    rain_status = Column(String)
    readable_warnings = Column(String)

def insert_weather_data(session, client, my_place, my_place_weather_forecast, day):
    # Convert day['dt'] from bigint to DateTime
    date = datetime.fromtimestamp(day['dt'])

    # Initialize values
    rain_status = "No rain forecast available."
    readable_warnings = {'result': "No weather alerts available."}
    weather_desc = "No weather description available."
    weather_icon = "No weather icon available."

    # Check if rain status, wheather and warnings are available
    if my_place_weather_forecast.position.get('rain_product_available'):
        # Fetch weather description and icon if available
        if day['weather12H']:
            weather_desc = day['weather12H']['desc']
            weather_icon = day['weather12H']['icon']
        # Fetch weather alerts
        if my_place.admin2 and len(my_place.admin2) < 3:
            my_place_weather_alerts = client.get_warning_current_phenomenoms(
                my_place.admin2
            )
            readable_warnings = readeable_phenomenoms_dict(
                my_place_weather_alerts.phenomenons_max_colors
            )
        my_place_rain_forecast = client.get_rain(my_place.latitude, my_place.longitude)
        next_rain_dt = my_place_rain_forecast.next_rain_date_locale()
        rain_status = "No rain expected in the following hour." if not next_rain_dt else next_rain_dt.strftime("%H:%M")

    weather_data = MeteoFrance(
        city=my_place.name,
        latitude=my_place_weather_forecast.position['lat'],
        longitude=my_place_weather_forecast.position['lon'],
        date=date,
        tmin=day['T']['min'],
        tmax=day['T']['max'],
        hmin=day['humidity']['min'],
        hmax=day['humidity']['max'],
        precipitation=day['precipitation']['24h'],
        sunrise=day['sun']['rise'],
        sunset=day['sun']['set'],
        weather_desc=weather_desc,
        weather_icon=weather_icon,
        rain_status=rain_status,
        readable_warnings=json.dumps(readable_warnings)
    )

    # Check if the date is greater than 14 days in the future
    if (weather_data.date.date() - datetime.now().date()).days > 14:
        # Add the weather data to the session
        print(f"Inserting data for {weather_data.city} on {weather_data.date.date()}")
        session.add(weather_data)
        # Commit the changes to the database
        session.commit()
    else:
        print(f"Skipping data for {weather_data.city} on {weather_data.date.date()} as it is already in the table.")
