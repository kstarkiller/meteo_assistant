FROM python:3.12-alpine

# Copier le contenu du répertoire meteofrance_data dans le conteneur
COPY . /app

# Définir le répertoire de travail
WORKDIR /app

# Installer les dépendances Python
RUN pip install --no-cache-dir -r report_gen_requirements.txt

# Exposer le port 8000
EXPOSE 8000

# Exécuter la commande pour démarrer l'application
CMD ["python3", "nlp.py"]