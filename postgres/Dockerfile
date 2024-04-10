# Utiliser une image Docker officielle de PostgreSQL comme base
FROM postgres:latest

# Récupérer les variables d'environnement pour PostgreSQL
ENV POSTGRES_USER $POSTGRES_USER
ENV POSTGRES_PASSWORD $POSTGRES_PASSWORD
ENV POSTGRES_DB $POSTGRES_DB

# Expose port 5432
EXPOSE 5432
