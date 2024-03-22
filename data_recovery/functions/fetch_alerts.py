from meteofrance_api.helpers import readeable_phenomenoms_dict

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
    return None