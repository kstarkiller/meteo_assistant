FROM python:3.12-alpine

# Installer le client PostgreSQL
RUN apk add --no-cache postgresql-client

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le contenu actuel du répertoire vers le répertoire /app dans le conteneur
COPY . .

# Variables d'environnement
ENV DB_NAME 'weather_forecast'
ENV USER 'postgres'
ENV PASSWORD 'pauline'
ENV DB_HOST '4.245.83.159'
ENV PORT '5432'

# Installer les dépendances Python
RUN pip install --no-cache-dir -r report_gen_requirements.txt

# Exposer le port 8000
EXPOSE 8000

# Exécuter la commande pour démarrer l'application
CMD ["python3", "nlp.py"]