# Utiliser une image Docker officielle de PostgreSQL comme base
FROM postgres:latest

# Définir les variables d'environnement
ENV POSTGRES_DB=weather_forecast
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=kevin
ENV POSTGRES_HOST=localhost
ENV POSTGRES_PORT=5432

EXPOSE 5432

# Exécuter la commande pour démarrer PostgreSQL
CMD ["postgres"]
