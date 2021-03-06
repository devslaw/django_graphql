"""
Django settings for django_graphql project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '# SECURITY WARNING: keep the secret key used in production secret!'

# SECURITY WARNING: don't run with debug turned on in production!

# Application definition

DEFAULT_APPS = [
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'graphene_django',
    'graph_auth',
]

PROJECT_APPS = [
    'apps.accounts',
    'apps.core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_graphql.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, '../templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_graphql.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'
# TIME_ZONE = 'Asia/Yerevan'

USE_I18N = True

USE_L10N = True

USE_TZ = True

ADMIN_EMAIL = 'info@devslaw.com'
SITE_EMAIL = 'info@devslaw.com'

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '../collectstatic')
STATIC_MEDIA_ROOT = os.path.join(BASE_DIR, '../static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '../static'),
)
# The default file storage backend used during the build process
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

MEDIA_ROOT = os.path.join(BASE_DIR, '../media')
MEDIA_URL = '/media/'

# Default user model.
AUTH_USER_MODEL = 'accounts.User'

# Email configs.
SENDER_EMAIL = 'info@devslaw.com'

GRAPH_AUTH = {
    'USER_FIELDS': ('first_name', 'last_name', 'username', 'email', 'is_superuser', 'active'),
    # Which username fields are available
    'ONLY_ADMIN_REGISTRATION': False,  # Only alow admins to register new users
    'WELCOME_EMAIL_TEMPLATE': None,  # Email template for optional welcome email, user object fields is in scope
    'EMAIL_FROM': 'test@gmail.com'  # Email from for welcome email
}

GRAPHENE = {
    'SCHEMA': 'django_graphql.schema.schema'
}

FIXTURE_DIRS = [os.path.join(BASE_DIR, '../fixtures/')]
