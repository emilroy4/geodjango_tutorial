#!/bin/bash

# Activate the conda environment
source activate awm-env

# Wait for PostgreSQL to be ready
echo "Waiting for PostgreSQL to be ready..."
until pg_isready -h $POSTGRES_HOST -p $POSTGRES_PORT -U $POSTGRES_USER; do
  sleep 2
done

# Run migrations
echo "Applying database migrations..."
python manage.py migrate

# Run the main container command
exec "$@"
