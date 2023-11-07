import os
from pathlib import Path

import environ

CORE_DIR = Path(__file__).resolve().parent
BASE_DIR = CORE_DIR.parent

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
PROJECT_NAME = env.str('PROJECT_NAME')
ENV = env.str('ENV')
VERSION = env.str('VERSION')

DEBUG = env.bool('DEBUG')
SECRET_KEY = env.str('SECRET_KEY')
ALLOWED_HOSTS = env.list('URLS')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # outer apps
    'rest_framework',
    'drf_spectacular',
    'corsheaders',
    'django_celery_results',

    # inner apps
    'file_upload',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env.str('POSTGRES_DB'),
        'USER': env.str('POSTGRES_USER'),
        'PASSWORD': env.str('POSTGRES_PASSWORD'),
        'HOST': env.str('POSTGRES_HOST'),
        'PORT': env.str('POSTGRES_PORT'),
    },
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# REST
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],

    # Для swagger'a
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

# SWAGGER
SPECTACULAR_SETTINGS = {
    'TITLE': 'FileProccess API',
    'DESCRIPTION': 'Endpoints for FileProccess API',
    'VERSION': 'v1',
    'SERVE_INCLUDE_SCHEMA': False,
    'LICENSE': {'name': 'BSD License'},
    'COMPONENT_SPLIT_REQUEST': True,

    'SERVE_PUBLIC': True,
    'SERVE_PERMISSIONS': ['rest_framework.permissions.AllowAny'],
}

# CORS
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

# CSRF
CSRF_TRUSTED_ORIGINS = tuple('http{}://{}'.format('' if ENV == 'local' else 's', x) for x in ALLOWED_HOSTS)


# REDIS
REDIS_LOGIN = env.str('REDIS_LOGIN')
REDIS_PASSWORD = env.str('REDIS_PASSWORD')
REDIS_HOST = env.str('REDIS_HOST')
REDIS_PORT = env.str('REDIS_PORT')
REDIS_URL = f'redis://{REDIS_LOGIN}:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}'

# Celery Configuration Options
CELERY_TIMEZONE = TIME_ZONE
CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_CACHE_BACKEND = 'django-cache'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_BROKER_URL = CELERY_RESULT_BACKEND = REDIS_URL
