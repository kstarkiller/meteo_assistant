#!/bin/bash

# Attendre que PostgreSQL soit prêt sur le port 5432
../scripts/wait-for-it.sh postgres:5432 --timeout=60 -- echo "PostgreSQL is up and running."

# Démarrer l'application
python daily_batch.py
