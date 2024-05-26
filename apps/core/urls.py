"""URLS do app CORE"""
from django.urls import path

from apps.core.views import HomeView

app_name: str = "core"

urlpatterns: list = [
    path("", HomeView.as_view(), name="home"),
]
