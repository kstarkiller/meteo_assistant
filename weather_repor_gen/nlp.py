import sys
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import json
import requests
from datetime import datetime, time

sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))
from hidden import B16_API_KEY

from retrieve_data_from_db import fetch_data_from_db

# Set the API key and the headers
headers = {"Authorization": "Bearer " + B16_API_KEY}
provider = "openai"
url = "https://api.edenai.run/v2/text/generation"

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

@app.post("/{city}/{date}/{hour}")
async def bot_request(city: str, date: str, hour: int):
    # Convert hour to time object
    hour = time(hour,0,0)

    # Fetch the weather data from the database
    weather_data = fetch_data_from_db(city, date, hour)

    payload = {
        "providers": "openai,cohere",
        "text": f"Donne-moi la météo d'après ces données brute : {weather_data}.",
        "temperature": 0.2,
        "max_tokens": 250,
        "fallback_providers": ""
    }

    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)[provider]

    return result['generated_text']

# Run the API with uvicorn on port 8000
uvicorn.run(app, host="0.0.0.0", port=8000)