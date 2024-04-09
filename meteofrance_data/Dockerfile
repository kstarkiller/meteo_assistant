# Utiliser une image de base appropriée
FROM python:3.12-alpine

# Installer le client PostgreSQL
RUN apk add --no-cache postgresql-client

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le contenu actuel du répertoire vers le répertoire /app dans le conteneur
COPY . .

# # Variables d'environnement
ENV DATABASE=weather_forecast
ENV USER=postgres
ENV PASSWORD=kevin
ENV HOST=localhost
ENV PORT=5432

# Installer les dépendances Python
RUN pip install --no-cache-dir -r mf_data_requirements.txt

# Exécuter la commande pour démarrer l'application
CMD ["python3", "daily_batch.py"]