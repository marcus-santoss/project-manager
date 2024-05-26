"""Módulo de Configurações de inicialização do app CORE"""
from django.apps import AppConfig


class CoreConfig(AppConfig):
    """Configurações de inicialização do app CORE"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.core"
