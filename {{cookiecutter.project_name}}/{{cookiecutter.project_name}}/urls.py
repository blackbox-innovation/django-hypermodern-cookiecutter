"""{{cookiecutter.project_name}} URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from baton.autodiscover import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.views.defaults import page_not_found
from django.views.generic.base import RedirectView
from django.views.i18n import JavaScriptCatalog


def trigger_error(request):
    return 1 / 0


# admin.autodiscover()
# admin.site.enable_nav_sidebar = False


def custom_page_not_found(request):
    return page_not_found(request, None)


urlpatterns = [
    path("health/", include("watchman.urls")),
    path("baton/", include("baton.urls")),
    path("verwaltung/", admin.site.urls),
    path("sentry-error-please/", trigger_error),
    path("", include("{{cookiecutter.project_name}}.apps.core.urls")),
    path("favicon.ico", RedirectView.as_view(url=settings.STATIC_URL + "images/favicon.ico")),
    path(
        "404/",
        custom_page_not_found,
    ),
    path("select2/", include("django_select2.urls")),
    path("jsi18n/", JavaScriptCatalog.as_view(), name="javascript-catalog"),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
