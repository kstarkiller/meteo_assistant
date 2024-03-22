import sys
import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from datetime import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir)))
from hidden import DATABASE, USER, PASSWORD, HOST, PORT

def connect_to_database():
    # Create the engine
    engine = create_engine(f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}')

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    return session

def fetch_data_from_db(ville, date, heure):
    # Connexion à la base de données
    conn = connect_to_database()

    # Requête SQL Alchemy pour récupérer les données de prévision météo
    query = text("""
        SELECT * FROM french_cities_weather 
        WHERE city = :city 
        AND date(date) = :date 
        AND EXTRACT(HOUR FROM date) = :hour
        AND EXTRACT(MINUTE FROM date) = :minute
    """)

    result = conn.execute(query, {"city": ville,
                                  "date": date,
                                  "hour": heure.hour,
                                  "minute": heure.minute})

    # Construction d'un dictionnaire à partir de result
    dict_result = {}
    for row in result:
        for i, column in enumerate(result.keys()):
            if column not in ['id', 'weather_icon','add_date']:
                dict_result[column] = row[i]
        
    return dict_result
