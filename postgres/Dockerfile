# Utiliser une image Docker officielle de PostgreSQL comme base
FROM postgres:latest

# Variables d'environnement
ENV POSTGRES_DB=weather_forecast
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=kevin
ENV POSTGRES_HOST=localhost
ENV POSTGRES_PORT=5432

# Expose port 5432
EXPOSE 5432

# Check if the server is ready to accept connections
HEALTHCHECK --interval=5s --timeout=3s --start-period=5s --retries=3 CMD pg_isready -U postgres || exit 1

# Exécuter la commande pour démarrer PostgreSQL
CMD ["postgres"]
