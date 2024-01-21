from .base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = ROOT_DIR / 'root'
STATICFILES_DIRS = [
    ROOT_DIR / 'static',
]

MEDIA_URL = 'media/'
MEDIA_ROOT = ROOT_DIR / 'uploads'
