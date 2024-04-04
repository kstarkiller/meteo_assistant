# Utiliser une image de base appropriée
FROM python:3.12-alpine

# Installer le client PostgreSQL
RUN apk add --no-cache postgresql-client

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le contenu actuel du répertoire vers le répertoire /app dans le conteneur
COPY . .

# variables d'environnement
ENV DATABASE 'weather_forecast'
ENV USER 'postgres'
ENV PASSWORD 'kevin'
ENV HOST 'postgres-container-v3.cwhtbmb9g9cxebgd.westeurope.azurecontainer.io'
ENV PORT '5432'

# Variables d'environnement
ARG DATABASE
ARG USER
ARG PASSWORD
ARG HOST
ARG PORT

ENV DATABASE=$DATABASE
ENV USER=$USER
ENV PASSWORD=$PASSWORD
ENV HOST=$HOST
ENV PORT=$PORT

# Installer les dépendances Python
RUN pip install --no-cache-dir -r mf_data_requirements.txt

# Exécuter la commande pour démarrer l'application
CMD ["python3", "daily_batch.py"]