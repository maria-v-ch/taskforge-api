"""Test settings for the project."""

from typing import Dict

from django.conf import settings

# Import specific settings we want to override
INSTALLED_APPS = settings.INSTALLED_APPS
MIDDLEWARE = settings.MIDDLEWARE
ROOT_URLCONF = settings.ROOT_URLCONF
AUTH_USER_MODEL = settings.AUTH_USER_MODEL
REST_FRAMEWORK = settings.REST_FRAMEWORK
SIMPLE_JWT = settings.SIMPLE_JWT
AUTH_PASSWORD_VALIDATORS = settings.AUTH_PASSWORD_VALIDATORS
LANGUAGE_CODE = settings.LANGUAGE_CODE
TIME_ZONE = settings.TIME_ZONE
USE_I18N = settings.USE_I18N
USE_TZ = settings.USE_TZ
STATIC_URL = settings.STATIC_URL
DEFAULT_AUTO_FIELD = settings.DEFAULT_AUTO_FIELD

# Use SQLite for testing
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

# Disable debugging
DEBUG = False

# Use a fast password hasher for testing
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

# Disable logging during tests
LOGGING: Dict = {}
