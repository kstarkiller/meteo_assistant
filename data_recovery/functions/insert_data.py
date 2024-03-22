import json
from datetime import datetime

from functions.weather_class import MeteoFrance
from functions.fetch_alerts import fetch_weather_alerts

def insert_weather_data(session, client, my_place, my_place_weather_forecast, hour):
    # Convert hour['dt'] from bigint to DateTime
    date = datetime.fromtimestamp(hour['dt'])

    # Initialize values
    readable_warnings = "No weather alerts available."
    weather_desc = "No weather description available."
    weather_icon = "No weather icon available."
    snow = "No snow forecast available."
    rain = "No rain forecast available."
    wind = "No wind forecast available."
    clouds = "No cloud forecast available."

    readable_warnings = fetch_weather_alerts(my_place, my_place_weather_forecast, client)

    weather_data = MeteoFrance(
        city=my_place.name,
        latitude=my_place_weather_forecast.position['lat'],
        longitude=my_place_weather_forecast.position['lon'],
        date=date,
        temperature=hour['T']['value'],
        humidity=hour['humidity'],
        rain=json.dumps(hour['rain']) if isinstance(hour['rain'], dict) else rain,
        snow=json.dumps(hour['snow']) if isinstance(hour.get('snow'), dict) else snow,
        clouds=hour['clouds'] if isinstance(hour['clouds'], int) else clouds,
        wind=json.dumps(hour['wind']) if isinstance(hour['wind'], dict) else wind,
        weather_desc= hour['weather']['desc'] if isinstance(hour['weather'], dict) else weather_desc,
        weather_icon= hour['weather']['icon'] if isinstance(hour['weather'], dict) else weather_icon,
        readable_warnings=json.dumps(readable_warnings),
        add_date=datetime.now()
    )

    # Check if the date is 4 days from now
    if (weather_data.date.date() - datetime.now().date()).days == 8 :
        # Add the weather data to the session
        session.add(weather_data)
        # Commit the changes to the database
        session.commit()

        return 1
    
    else:
        return 0

    
