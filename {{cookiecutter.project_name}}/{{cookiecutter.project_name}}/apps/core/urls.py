from django.urls import include, path
from django.views.generic import TemplateView


urlpatterns = [
    path("", TemplateView.as_view(template_name='empty.html'), name="dashboard"),
    path("accounts/", include("allauth.urls")),
 
]
