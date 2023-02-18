from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CoreConfig(AppConfig):
    label = "core"
    name = "{{cookiecutter.project_name}}.apps.core"
    verbose_name = _("general")

    def ready(self):
        import {{cookiecutter.project_name}}.apps.core.signals  # noqa
