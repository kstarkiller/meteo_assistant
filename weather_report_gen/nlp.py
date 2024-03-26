import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
import io
import uvicorn
import json
import requests
from datetime import time
from typing import Optional
import base64

import logging
from logging.handlers import RotatingFileHandler
import uuid

# Create a rotating file handler
log_handler = RotatingFileHandler(filename='logs/app.log', mode='a', backupCount=5, encoding='utf-8', delay=False)
log_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

# Get the root logger and add the handler
logger = logging.getLogger()
logger.addHandler(log_handler)
logger.setLevel(logging.INFO)

B16_API_KEY = os.getenv("B16_API_KEY")

from retrieve_data_from_db import fetch_data_from_db

# Set the API key and the headers
headers = {"Authorization": "Bearer " + B16_API_KEY}
text_provider = "openai"
speech_provider = "google"
text_url = "https://api.edenai.run/v2/text/generation"
speech_url = "https://api.edenai.run/v2/audio/text_to_speech"

text_payload = {
            "response_as_dict": True,
            "attributes_as_list": False,
            "show_original_response": False,
            "providers": text_provider,
            "temperature": 0.2,
            "max_tokens": 250,
        }

speech_payload = {
        "response_as_dict": True,
        "attributes_as_list": False,
        "show_original_response": False,
        "rate": 0,
        "pitch": 0,
        "volume": 0,
        "sampling_rate": 0,
        "providers": speech_provider,
        "language": "fr-FR",
        "option": "FEMALE" 
    }

app = FastAPI()

# Allow CORS
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/test/{prompt}")
async def read_item(prompt):
    return {"It works"}

@app.post("/weather_request/")
async def bot_request(city: str, date: str, hour: Optional[int] = None):
    request_id = uuid.uuid4()
    logging.info('Received a request with ID: %s for city: %s, date: %s, hour: %s', request_id, city, date, hour)

    if hour is not None:
        # Convert hour to time object
        hour = time(hour, 0, 0)

    # Fetch the weather data from the database
    weather_data = fetch_data_from_db(city, date, hour)
    logging.info('Request ID %s : Fetched weather data: %s', request_id, weather_data)
    
    if weather_data == "Ville non reconnue.":
        logging.error('Request ID %s : City not recognized: %s', request_id, city)
        return "Ville non reconnue."
    else:
        text_payload["text"] = f"Donne moi un bulletin météo pour {city} le {date}, uniquement basé sur ces données : {weather_data}. Et ne fais aucune mention de la précision des données."

    text_response = requests.post(text_url, json=text_payload, headers=headers)
    text_result = json.loads(text_response.text)[text_provider]['generated_text']
    logging.info('Request ID %s : Text successfully generated', request_id)

    # Get the speech response
    speech_payload["text"] = text_result
    speech_response = requests.post(speech_url, json=speech_payload, headers=headers)
    speech_result = json.loads(speech_response.text)[speech_provider]['audio']
    
    if text_response.status_code == 200:
        if speech_response.status_code == 200:
            if speech_result:
                audio_bytes = base64.b64decode(speech_result)
                with open(f"logs/store/{request_id}.mp3", "wb") as f:
                    f.write(audio_bytes)
                print(text_result)
                logging.info('Request ID %s : Audio successfully generated audio', request_id)
                return StreamingResponse(io.BytesIO(audio_bytes), media_type="audio/mpeg")
            
            else:
                logging.error('Request ID %s : No audio data available in the response', request_id)
                return "Aucune donnée audio disponible dans la réponse."
            
        else:
            logging.error('Request ID %s : Error in speech request: %s - %s', request_id, speech_response.status_code, speech_response.text)
            return f"Erreur lors de la requête audio : {speech_response.status_code} - {speech_response.text}"    
    else:
        logging.error('Request ID %s : Error in text request: %s - %s', request_id, text_response.status_code, text_response.text)
        return f"Erreur lors de la requête texte : {text_response.status_code} - {text_response.text}"


# Run the API with uvicorn on port 8000
uvicorn.run(app, host="0.0.0.0", port=8000)