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

EXPOSE 5432

# Exécuter la commande pour démarrer PostgreSQL
CMD ["postgres"]
