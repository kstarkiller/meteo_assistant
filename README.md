# Mateo - AI based weather assistant

## Introduction
Mateo is an AI-based weather assistant designed to provide real-time weather information and forecasts. With Mateo, you can easily access accurate weather data for french cities. Whether you're planning a trip, organizing outdoor activities, or simply curious about the weather, Mateo has got you covered. Powered by advanced machine learning algorithms, Mateo delivers precise french audio weather predictions and personalized recommendations to help you make informed decisions. Say goodbye to unexpected weather surprises and let Mateo be your ultimate weather companion.

Weather datas are provided by Meteo France.
For more information on the Meteo France API, you can visit the [official documentation](https://meteofrance-api.readthedocs.io/en/latest/).

## Getting Started
### Project Organization
```
simplon_brief16_meteo_assistant/
├── front/
│   ├── Dockerfile
│   ├── index.html
│   ├── meteo-scaled.jpg (background image)
│   ├── script.js
│   └── styles.css
├── meteofrance_data/
│   ├── functions/
│   │   ├── db_and_table_init.py
│   │   ├── delete_data.py
│   │   ├── fetch_data.py
│   │   ├── insert_data.py
│   │   ├── weather_class.py
│   │   └── test_api.py
│   ├── Dockerfile
│   ├── cities.py
│   ├── daily_batch.py
│   └── mf_data_requirements.txt
├── postgres/
│   └── Dockerfile
├── weather_report_gen/
│   ├── Dockerfile
│   ├── nlp.py
│   ├── retrieve_data_from_db.py
│   └── report_gen_equirements.txt
├── .gitignore
└── README.md
```

### Installation
1. Install Docker on your system
There are many ways to install Docker depending on your system and preferences but I advise you to install Docker Desktop : it simple to install and to use.
To install Docker Desktop if not already done, you can visit the [official Docker website](https://www.docker.com/products/docker-desktop/).

2. Create a docker-compose.yml file to run images from each Dockerfile
Here is the template of the docker-compose file I used :
 INSERT EXEMPLE

You can create the docker-compose wherever you want but make sure to replace paths to the Dockerfiles with your own absolute paths.
Also, you must replace environnements variables by your owns, especially the Eden AI API KEY.

    If you don't have Eden AI API KEY :
        > Visit the Eden AI website.
        > Register for an account and retrieve your API key from the user dashboard.

3. Run the docker-compose file:
```bash
cd path/to/your/docker-compose/file
docker-compose up -d
```

4. Run the Mateo application
Open you browser and go to http://localhost:8080 (if you didn't change HOST and PORT in the docker-compose).