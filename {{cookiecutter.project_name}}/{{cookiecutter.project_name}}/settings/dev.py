import logging
from logging.handlers import RotatingFileHandler

from .base import *  # noqa
from .base import INSTALLED_APPS, MIDDLEWARE

DEBUG = True

ALLOWED_HOSTS = ["*"]

DEV_APPS = [
    "debug_toolbar",
]
# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = INSTALLED_APPS + DEV_APPS

MIDDLEWARE = MIDDLEWARE + [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

INTERNAL_IPS = [
    "127.0.0.1",
]

CELERY_BROKER_URL = "redis://localhost:6379/0"
CELERY_TASK_DEFAULT_QUEUE = "{{cookiecutter.project_name}}"


DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"
MEDIA_ROOT = "./media/"
MEDIA_URL = "/media/"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    },
    "compressor": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    },
}

COMPRESS_CACHE_BACKEND = "compressor"
# https://django-compressor.readthedocs.io/en/2.1/scenarios/
COMPRESS_OFFLINE = False


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
        "": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": True,
        },
        "django.db.backends": {"handlers": ["console"], "level": "DEBUG"},
    },
}

# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "handlers": {
#         "django_rich_logging": {
#             "class": "django_rich_logging.logging.DjangoRequestHandler",
#             "level": "INFO",
#         },
#     },
#     "loggers": {
#         "django.server": {"handlers": ["django_rich_logging"], "level": "INFO"},
#         "django.request": {"level": "CRITICAL"},
#     },
# }

# https://django-compressor.readthedocs.io/en/stable/settings.html
COMPRESS_PRECOMPILERS = (
    ("text/x-scss", "echo {infile} {outfile} >> /tmp/sass && sass {infile} {outfile}"),
    (
        "text/javascript",
        "./node_modules/.bin/esbuild --sourcemap=inline --bundle {infile} --outfile={outfile}",
    ),
)


logger_file_handler = RotatingFileHandler("./test.log")
logger_file_handler.setLevel(logging.DEBUG)

logging.captureWarnings(True)

root_logger = logging.getLogger()

root_logger.addHandler(logger_file_handler)
root_logger.setLevel(logging.DEBUG)
