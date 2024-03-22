import unittest
from meteofrance_api import MeteoFranceClient
from fetch_data import fetch_weather_alerts, fetch_api_forecast

class TestMeteoFranceAPI(unittest.TestCase):
    def setUp(self):
        self.client = MeteoFranceClient()

    def test_api_connection(self):
        # Test if we can successfully connect to the API
        self.assertIsNotNone(self.client)

    def test_fetch_weather_data(self):
        # Test if we can fetch weather data for a few cities
        cities = ["Paris", "Lyon", "Marseille"]
        for city in cities:
            place = self.client.search_places(city)
            self.assertIsNotNone(place)
            forecast = self.client.get_forecast_for_place(place[0])
            self.assertIsNotNone(forecast)
            self.assertIsNotNone(forecast.raw_data)

    def test_fetch_api_forecast(self):
        # Test if we can fetch weather forecast for a few cities
        cities = ["Montpellier", "Jacou", "Fort-de-France"]
        for city in cities:
            client, my_place, my_place_weather_forecast, my_place_hourly_forecast = fetch_api_forecast(city)
            self.assertIsNotNone(client)
            self.assertIsNotNone(my_place)
            self.assertIsInstance(my_place, object)
            self.assertIsNotNone(my_place_weather_forecast)
            self.assertIsInstance(my_place_weather_forecast, object)
            self.assertIsNotNone(my_place_hourly_forecast)
            self.assertIsInstance(my_place_hourly_forecast, list)
            self.assertIsNotNone(my_place_weather_forecast.raw_data)
            self.assertIsInstance(my_place_weather_forecast.raw_data, dict)

    def test_fetch_weather_alerts(self):
        # Test if we can fetch weather alerts for a few cities
        cities = ["Nantes", "Tours", "Mamoudzou"]
        for city in cities:
            client, my_place, my_place_weather_forecast, my_place_hourly_forecast = fetch_api_forecast(city)
            readable_warnings = fetch_weather_alerts(my_place, my_place_weather_forecast, client)
            self.assertIsNotNone(readable_warnings)
            if city in ["Nantes", "Tours"]:
                self.assertIsInstance(readable_warnings, dict)
                self.assertNotEqual(readable_warnings, "No weather alerts available.")
            else :
                self.assertNotEqual(readable_warnings, {})
                self.assertEqual(readable_warnings, "No weather alerts available.")


if __name__ == "__main__":
    unittest.main()