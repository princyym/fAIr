"""
Django settings for aiproject project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.aiproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.aiproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os 
import environ

env = environ.Env()
# reading .env file
environ.Env.read_env()

# Quick-start development settings - unsuitable for production
# See https://docs.aiproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
# if not env("SECRET_KEY"):
#     print("WARNING: secret key not set - setting a default for development.")
# if 'SECRET_KEY' not in os.environ:
#     SECRET_KEY='yl2w)c0boi_ma-1v5)935^2#&m*r!1s9z9^*9e5co^08_ixzo6'

if 'SECRET_KEY' not in env:
    print("WARNING: secret key not set - setting a default for development.")
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
else:
    SECRET_KEY = env("SECRET_KEY")
# SECURITY WARNING: don't run with debug turned on in production!
if 'DEBUG' not in env:
    DEBUG = True
else :
    DEBUG=env("DEBUG")

if 'ALLOWED_HOSTS' not in env:
    ALLOWED_HOSTS = []
else :
    ALLOWED_HOSTS=[env("ALLOWED_HOSTS")]

if 'GDAL_LIBRARY_PATH' not in env:
    pass
else:
    GDAL_LIBRARY_PATH = env('GDAL_LIBRARY_PATH')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'django.contrib.gis',
    'leaflet',
    'rest_framework',
    'rest_framework_gis',
    'rest_framework_swagger',
    'django_filters',
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

if 'CORS_ALLOWED_ORIGINS' not in env:
    CORS_ORIGIN_ALLOW_ALL = True
    CORS_ALLOW_HEADERS = ['*']
else:
    CORS_ALLOWED_ORIGINS=[env('CORS_ALLOWED_ORIGINS')]

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_AUTHENTICATION_CLASSES': [
    ],
}

ROOT_URLCONF = 'aiproject.urls'

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
            'libraries': {  
                'staticfiles': 'django.templatetags.static',
                },
        },

    },
]

WSGI_APPLICATION = 'aiproject.wsgi.application'


# Database
# https://docs.aiproject.com/en/3.1/ref/settings/#databases
if 'DATABASE_NAME' not in env:
    DATABASES = {
        'default': {        
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME': 'ai',
            'USER': 'admin',
            'PASSWORD': 'password',
            'HOST': 'localhost',
            'PORT': 5432,
        }
    }
else:
     DATABASES = {
        'default': {        
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME': env('DATABASE_NAME'),
            'USER': env('DATABASE_USER'),
            'PASSWORD': env('DATABASE_PASSWORD'),
            'HOST': env('DATABASE_HOST'),
            'PORT': env('DATABASE_PORT'),
        }
    }



# Password validation
# https://docs.aiproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.aiproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.aiproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

