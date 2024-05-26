"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views.:
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("apps.core.urls", namespace="core")),
    path("project/", include("apps.project.urls", namespace="project")),
    path("admin/", admin.site.urls),
]
