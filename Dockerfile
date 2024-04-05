# Utiliser une image Docker officielle de PostgreSQL comme base
FROM postgres:latest

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

# Expose port 5432
EXPOSE 5432

# Check if the server is ready to accept connections
HEALTHCHECK --interval=5s --timeout=3s --start-period=5s --retries=3 CMD pg_isready -U postgres || exit 1

# Exécuter la commande pour démarrer PostgreSQL
CMD ["postgres"]
