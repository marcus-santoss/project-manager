"""Módulo de Views do App CORE"""

from django.views.generic import TemplateView


class Dashboard(TemplateView):
    """View para HomePage"""

    template_name = "core/base.html"
