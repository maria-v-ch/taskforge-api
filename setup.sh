#!/bin/bash

# Create and activate virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    python -m venv .venv
fi

# Activate virtual environment
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Navigate to the Django project directory
cd todolist

# Terminate existing connections to the database
PGPASSWORD=$DB_PASSWORD psql -U $DB_USER -d postgres -c "
SELECT pg_terminate_backend(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE pg_stat_activity.datname = 'todolist'
AND pid <> pg_backend_pid();"

# Drop and recreate database
PGPASSWORD=$DB_PASSWORD psql -U $DB_USER -d postgres -c "DROP DATABASE IF EXISTS todolist;"
PGPASSWORD=$DB_PASSWORD psql -U $DB_USER -d postgres -c "CREATE DATABASE todolist;"

# Run migrations
python manage.py makemigrations users
python manage.py makemigrations todolist_app
python manage.py migrate

# Create superuser if it doesn't exist
echo "from users.models import User; User.objects.filter(email='admin@example.com').exists() or User.objects.create_superuser(username='admin', email='admin@example.com', password='admin123')" | python manage.py shell

echo "Setup completed successfully! You can now run: python manage.py runserver"
