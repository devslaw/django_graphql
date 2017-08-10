# django_graphql
Django/GraphQL api

Create virtualenv

    cd /var/envs && mkvirtualenv --python=/usr/bin/python3 django_graphql_example

Install requirements for a project.

    cd /var/www/django_graphql && pip install -r requirements/local.txt

Make migrations and migrate

    python manage.py makemigrations
    python manage.py migrate
