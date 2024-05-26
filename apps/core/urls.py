"""URLS do app CORE"""

from django.urls import path

from apps.core.views import Dashboard

app_name: str = "core"

urlpatterns: list = [
    path("", Dashboard.as_view(), name="dashboard"),
]
