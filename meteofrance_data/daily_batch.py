from functions.db_and_table_init import connect_to_database, create_table
from functions.insert_data import insert_weather_data
from functions.delete_data import delete_all_data
from functions.fetch_data import fetch_api_forecast
from cities import cities

# Connect to the database
conn = connect_to_database()

# Create the table if it doesn't exist
create_table(conn)

# Delete all data from the table as predictions have changed
delete_all_data(conn)

# Iterate over cities and fetch weather data    
for c in cities:
    client, my_place, my_place_weather_forecast, my_place_hourly_forecast = fetch_api_forecast(c)

    # Insert the data into the database
    total = 0
    for hour in my_place_hourly_forecast:
        total += insert_weather_data(conn, client, my_place, my_place_weather_forecast, hour)
    
    print(f"{total} rows inserted for {my_place.name}.")

# Close the connection
conn.close()
