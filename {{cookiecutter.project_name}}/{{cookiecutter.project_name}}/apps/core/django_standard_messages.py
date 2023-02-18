from django.utils.translation import gettext_lazy as _

# https://stackoverflow.com/questions/7878028/override-default-django-translations

lambda s: s
django_standard_messages_to_override = [
    _("History"),
    _("axes"),
    _("You have signed out."),
    _("Constance"),
]
