from django import template
from django.core.files.storage import get_storage_class
from django.urls import reverse_lazy

register = template.Library()



@register.inclusion_tag("inclusion_tags/avatar.html")
def avatar(user, size="md", additional_classes="", id=""):
    return {
        "size": size,
        "user": user,
        "additional_classes": additional_classes,
        "id": id,
    }


@register.simple_tag(takes_context=True)
def get_active_class(context, url_to_check: str) -> str:
    request = context["request"]
    if request.get_full_path() == reverse_lazy(url_to_check):
        # this could be in the settings or in the app config
        return "active"
    return ""


