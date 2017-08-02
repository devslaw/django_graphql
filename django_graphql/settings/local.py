# -*- coding: utf-8 -*-

from django_graphql.settings.base import *

DEBUG = True
THUMBNAIL_DEBUG = True

BASE_URL = 'http://127.0.0.1:8000/'

ALLOWED_HOSTS = ['*', ]

INSTALLED_APPS = DEFAULT_APPS + PROJECT_APPS

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'graphql',
        'USER': 'graphql',
        'PASSWORD': 'graphql',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}
