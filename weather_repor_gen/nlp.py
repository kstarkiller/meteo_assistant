import sys
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import json
import requests
from datetime import time
from typing import Optional
import base64

sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))
from hidden import B16_API_KEY

from retrieve_data_from_db import fetch_data_from_db

# Set the API key and the headers
headers = {"Authorization": "Bearer " + B16_API_KEY}
text_provider = "mistral"
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
        "language": "en-GB",
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
    if hour is not None:
        # Convert hour to time object
        hour = time(hour, 0, 0)

    # Fetch the weather data from the database
    if hour:
        weather_data = fetch_data_from_db(city, date, hour)
        text_payload["text"] = f"Donne-moi la météo à {hour} pour {city} : {weather_data}."

    else:
        weather_data = fetch_data_from_db(city, date)
        text_payload["text"] = f"Donne-moi la météo moyenne du jour pour {city} : {weather_data}."

    text_response = requests.post(text_url, json=text_payload, headers=headers)
    text_result = json.loads(text_response.text)[text_provider]['generated_text']

    # Get the speech response
    speech_payload["text"] = text_result
    speech_response = requests.post(speech_url, json=speech_payload, headers=headers)
    speech_result = json.loads(speech_response.text)[speech_provider]['audio']
    
    if text_response.status_code == 200:
        if speech_response.status_code == 200:
            if speech_result:
                audio_bytes = base64.b64decode(speech_result)
                with open("audio_result/audio.mp3", "wb") as audio_file:
                    audio_file.write(audio_bytes)
                print(text_result)
                return audio_bytes
            
            else:
                return "Aucune donnée audio disponible dans la réponse."
            
        else:
            return f"Erreur lors de la requête audio : {speech_response.status_code} - {speech_response.text}"
        
    else:
        return f"Erreur lors de la requête texte : {text_response.status_code} - {text_response.text}"


# Run the API with uvicorn on port 8000
uvicorn.run(app, host="0.0.0.0", port=8000)