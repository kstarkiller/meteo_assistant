FROM python:3.12-alpine

# Installer le client PostgreSQL
RUN apk add --no-cache postgresql-client

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le contenu actuel du répertoire vers le répertoire /app dans le conteneur
COPY . .

# Variables d'environnement
ENV DATABASE=weather_forecast
ENV USER=postgres
ENV PASSWORD=kevin
ENV HOST=localhost
ENV PORT=5432
ENV API_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNjA5ZTFhOTMtMjZhYi00NTY3LTliODItZDk2NTk4YmNhODIyIiwidHlwZSI6ImFwaV90b2tlbiJ9.IP0_jpdfxZPAhu6R7bT64EPEXNWz2uml2YX6nzSY61I

# Installer les dépendances Python
RUN pip install --no-cache-dir -r report_gen_requirements.txt

# Exposer le port 8000
EXPOSE 8000

# Exécuter la commande pour démarrer l'application
CMD ["python3", "nlp.py"] 