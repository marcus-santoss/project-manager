"""Módulo de Views do App CORE"""

from django.urls import reverse_lazy
from django.views.generic import RedirectView


class HomePageRedirect(RedirectView):
    """Redireciona para a página de listagem de projetos"""

    permanent = True

    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy("project:project.list")
