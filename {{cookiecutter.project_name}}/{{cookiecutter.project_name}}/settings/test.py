import environ

from .base import *  # noqa

env = environ.Env()
LANGUAGE_CODE = "en"


# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#test-runner
TEST_RUNNER = "django.test.runner.DiscoverRunner"

# CACHES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}

# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]


# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

# Your stuff...
# ------------------------------------------------------------------------------
STATICFILES_STORAGE = "inmemorystorage.InMemoryStorage"
DEFAULT_FILE_STORAGE = "inmemorystorage.InMemoryStorage"

# https://django-axes.readthedocs.io/en/latest/2_installation.html?highlight=test#disabling-axes-components-in-tests
AXES_ENABLED = False


# https://stackoverflow.com/questions/22233680/in-memory-broker-for-celery-unit-tests
BROKER_BACKEND = "memory"
CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPAGATES = True

# https://django-compressor.readthedocs.io/en/stable/settings.html
# do not run any precompilers when running tests
COMPRESS_ENABLED = False
COMPRESS_PRECOMPILERS = ()

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        },
    },
    "handlers": {
        "default": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "standard",
            "stream": "ext://sys.stdout",
        },
    },
    "loggers": {
        "django.db.backends": {
            "level": "DEBUG",
            "handlers": ["default"],
            "propagate": False,
        },
    },
}
