from datetime import datetime, timedelta
from sqlalchemy import delete

from functions.weather_class import MeteoFrance

def delete_former_data(session):
    # Calculate the date for comparison (today - 1 day)
    yesterday = datetime.now() - timedelta(days=1)
    
    # Create a delete statement
    delete_statement = delete(MeteoFrance).where(MeteoFrance.date <= datetime.now())
    
    # Execute the delete statement
    session.execute(delete_statement)
    session.commit()
