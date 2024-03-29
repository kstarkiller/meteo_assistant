# Utiliser une image de base appropriée
FROM python:3.12-alpine

# Copier le contenu du répertoire meteofrance_data dans le conteneur
COPY . /app

# Définir le répertoire de travail
WORKDIR /app

# Installer les dépendances Python
RUN pip install --no-cache-dir -r mf_data_requirements.txt

# Exécuter la commande pour démarrer l'application
CMD ["python3", "daily_batch.py"]