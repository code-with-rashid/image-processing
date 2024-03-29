import os

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# Override settings for local development
if 'DOCKER_ENV' not in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ROOT_DIR / 'db.sqlite3',
        }
    }


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = ROOT_DIR / 'root'
STATICFILES_DIRS = [
    ROOT_DIR / 'static',
]

MEDIA_URL = 'media/'
MEDIA_ROOT = ROOT_DIR / 'uploads'
