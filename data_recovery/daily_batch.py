from meteofrance_api import MeteoFranceClient

from cities import cities
from functions.db_and_table_init import connect_to_database, create_table
from functions.insert_data import insert_weather_data
from functions.delete_data import delete_past_data, delete_data_to_update

# Init client
client = MeteoFranceClient()

# Connect to the database
conn = connect_to_database()

# Create the table if it doesn't exist
create_table(conn)

# Delete data to update
delete_data_to_update(conn)

# Iterate over cities and fetch weather data
for c in cities:
    # Search a location from name
    list_places = client.search_places(c)
    my_place = list_places[0]

    # Fetch weather forecast for the location
    my_place_weather_forecast = client.get_forecast_for_place(my_place)
    
    # Get the hourly forecast
    my_place_hourly_forecast = my_place_weather_forecast.forecast

    # Insert the data into the database
    total = 0
    for hour in my_place_hourly_forecast:
        total += insert_weather_data(conn, client, my_place, my_place_weather_forecast, hour)
    
    print(f"{total} rows inserted for {my_place.name}.")

# Delete former data
delete_past_data(conn)
print("Former data deleted.")

# Close the connection
conn.close()
