#!/bin/sh

# Chemin vers le fichier de secrets
CONFIG_FILE="config.py"

# Lire les valeurs des variables d'environnement à partir du fichier de secrets
POSTGRES_DB=$(grep DATABASE $CONFIG_FILE | cut -d ':' -f 2 | xargs)
POSTGRES_USER=$(grep USER $CONFIG_FILE | cut -d ':' -f 2 | xargs)
POSTGRES_PASSWORD=$(grep PASSWORD $CONFIG_FILE | cut -d ':' -f 2 | xargs)
PORT=$(grep PORT $CONFIG_FILE | cut -d ':' -f 2 | xargs)
HOST=$(grep HOST $CONFIG_FILE | cut -d ':' -f 2 | xargs)

# Configurer la base de données PostgreSQL avec les valeurs lues
export PGDATA=/var/lib/postgresql/data/pgdata
initdb -D $PGDATA
pg_ctl -D $PGDATA -o "-c listen_addresses='*' -c port=$PORT" start

# Créer la base de données et l'utilisateur
psql -c "CREATE DATABASE $POSTGRES_DB;"
psql -c "CREATE USER $POSTGRES_USER WITH ENCRYPTED PASSWORD '$POSTGRES_PASSWORD';"
psql -c "GRANT ALL PRIVILEGES ON DATABASE $POSTGRES_DB TO $POSTGRES_USER;"

# Arrêter le serveur PostgreSQL
pg_ctl -D $PGDATA stop

# Démarrer le serveur PostgreSQL avec les paramètres de configuration
pg_ctl -D $PGDATA -o "-c listen_addresses='*' -c port=$PORT" start
