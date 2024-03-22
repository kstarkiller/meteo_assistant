from meteofrance_api import MeteoFranceClient
from meteofrance_api.helpers import readeable_phenomenoms_dict

# Init client
client = MeteoFranceClient()


def fetch_api_forecast(city):
    # Search a location from name
    list_places = client.search_places(city)
    my_place = list_places[0]

    # Fetch weather forecast for the location
    my_place_weather_forecast = client.get_forecast_for_place(my_place)
    
    # Get the hourly forecast
    my_place_hourly_forecast = my_place_weather_forecast.forecast

    return client, my_place, my_place_weather_forecast, my_place_hourly_forecast


def fetch_weather_alerts(my_place, my_place_weather_forecast, client):
    # Check if rain status, weather and warnings are available
    if my_place_weather_forecast.position.get('rain_product_available'):
        # Fetch weather alerts
        if my_place.admin2 and len(my_place.admin2) < 3:
            my_place_weather_alerts = client.get_warning_current_phenomenoms(
                my_place.admin2
            )
            readable_warnings = readeable_phenomenoms_dict(
                my_place_weather_alerts.phenomenons_max_colors
            )
            return readable_warnings
    return "No weather alerts available."