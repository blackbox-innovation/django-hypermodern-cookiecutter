import sentry_sdk
from sentry_sdk.integrations.celery import CeleryIntegration
from sentry_sdk.integrations.django import DjangoIntegration

from .base import *  # noqa
from .base import INSTALLED_APPS, env, os

# AWS
AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")


# Mailjet
ANYMAIL = {
    "MAILJET_API_KEY": env("MAILJET_API_KEY"),
    "MAILJET_SECRET_KEY": env("MAILJET_SECRET_KEY"),
}


sentry_sdk.init(
    dsn=env("SENTRY_DSN"),
    integrations=[DjangoIntegration(), CeleryIntegration()],
    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True,
)
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES["default"]["ATOMIC_REQUESTS"] = True  # noqa F405
DATABASES["default"]["CONN_MAX_AGE"] = env.int("CONN_MAX_AGE", default=60)  # noqa F405

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": (
                "%(asctime)s [%(process)d] [%(levelname)s] "
                "pathname=%(pathname)s lineno=%(lineno)s "
                "funcname=%(funcName)s %(message)s"
            ),
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "handlers": {
        "null": {
            "level": "DEBUG",
            "class": "logging.NullHandler",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "ex_logger": {
            "handlers": [
                "console",
            ],
            "level": "INFO",
        }
    },
}

DEBUG = False

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(" ")

STATIC_HOST = os.environ.get("DJANGO_STATIC_HOST", "")
STATIC_URL = STATIC_HOST + "/static/"
AWS_STORAGE_BUCKET_NAME = env("S3_BUCKET")

PROD_APPS_START = []
# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = PROD_APPS_START + INSTALLED_APPS


# Force redirect
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = True

# https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# https://docs.djangoproject.com/en/3.0/ref/middleware/#http-strict-transport-security
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True


# https://github.com/Kozea/WeasyPrint/issues/220#issuecomment-305830750
CELERYD_MAX_TASKS_PER_CHILD = 10

# https://docs.celeryproject.org/en/latest/django/first-steps-with-django.html

# Celery
# ------------------------------------------------------------------------------
CELERY_BROKER_URL = env("REDIS_URL")
CELERY_TASK_DEFAULT_QUEUE = "{{cookiecutter.project_name}}"

# Executes various tasks
CELERY_BEAT_SCHEDULE = {
}
