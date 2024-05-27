"""URLS do app CORE"""

from django.urls import path

from apps.core.views import HomePageRedirect

app_name: str = "core"

urlpatterns: list = [
    path("", HomePageRedirect.as_view(), name="dashboard"),
]
