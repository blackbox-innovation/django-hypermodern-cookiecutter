from axes.apps import AppConfig
from django.utils.translation import gettext_lazy as _


# needed for app name translation
class AxesConfig(AppConfig):
    verbose_name = _("axes")
