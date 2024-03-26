import sys
import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir)))
# from hidden import DATABASE, USER, PASSWORD, HOST, PORT

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
# from meteofrance_data.cities import cities

# Import the required environment variables
DATABASE = os.getenv("DATABASE")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")

from cities import cities

def connect_to_database():
    # Create the engine
    engine = create_engine(f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}')

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    return session

def fetch_data_from_db(ville, date, heure=None):
    # Connexion à la base de données
    conn = connect_to_database()

    if ville not in cities:
        return "Ville non reconnue."
    
    else :
        # Requête SQL Alchemy pour récupérer les données de prévision météo
        if not heure:
            query = text("""
                SELECT * FROM french_cities_weather 
                WHERE city = :city 
                AND date(date) = :date 
            """)
            result = conn.execute(query, {"city": ville,
                                    "date": date})
        else:
            query = text("""
                SELECT * FROM french_cities_weather 
                WHERE city = :city 
                AND date(date) = :date 
                AND EXTRACT(HOUR FROM date) = :hour""")

            result = conn.execute(query, {"city": ville,
                                    "date": date,
                                    "hour": heure.hour})
    
        # Construction d'un dictionnaire à partir de result
        day_result = []
        hour_result = {}
        for row in result:
            for i, column in enumerate(result.keys()):
                if column not in ['id', 'latitude', 'longitude',
                                'readable_warnings','weather_icon','add_date']:
                    hour_result[column] = row[i]

            day_result.append(hour_result)

        return day_result
