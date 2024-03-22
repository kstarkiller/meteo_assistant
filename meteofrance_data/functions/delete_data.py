from datetime import datetime, timedelta
from sqlalchemy import delete

from functions.weather_class import MeteoFrance

def delete_past_data(session):
    # Create a delete statement
    delete_statement = delete(MeteoFrance).where(MeteoFrance.date <= datetime.now())
    
    # Execute the delete statement
    session.execute(delete_statement)
    session.commit()

def delete_data_to_update(session):
    # Create a delete statement
    delete_statement = delete(MeteoFrance).where(MeteoFrance.date >= datetime.now() + timedelta(days=2),
                                                 MeteoFrance.date <= datetime.now() + timedelta(days=3))
    
    # Execute the delete statement
    session.execute(delete_statement)
    session.commit()

def delete_all_data(session):
    # Create a delete statement
    delete_statement = delete(MeteoFrance)
    
    # Execute the delete statement
    session.execute(delete_statement)
    session.commit()