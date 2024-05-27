"""Views do app Project."""

from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from apps.core.mixins import DefaultContextMixin
from apps.project.models import Project


class ProjectCreateView(DefaultContextMixin, CreateView):
    """Django Class Based View para criação de um projeto"""

    model = Project
    """Modelo que esta view manipula"""
    template_name = "core/crud/form.html"
    """Nome do template utilizado para renderização do HTML"""
    success_url = reverse_lazy("project:project.list")
    """URL de Sucesso"""
    success_message = "Projeto Criado com Sucesso!"
    """Mensagem de Sucesso"""
    fields = ("title", "overview", "assigned_to", "start_date", "dead_line")
    """Campos a serem manipulados"""


class ProjectUpdateView(DefaultContextMixin, UpdateView):
    """Django Class Based View para atualização dos dados de um projeto"""

    model = Project
    """Modelo que esta view manipula"""
    template_name = "core/crud/form.html"
    """Nome do template utilizado para renderização do HTML"""
    success_url = reverse_lazy("project:project.list")
    """URL de Sucesso"""
    success_message = "Projeto Criado com Sucesso!"
    """Mensagem de Sucesso"""
    fields = ("title", "overview", "assigned_to", "start_date", "dead_line")
    """Campos a serem manipulados"""


class ProjectListView(DefaultContextMixin, ListView):
    """Django Class Based View para listagem de projetos"""

    model = Project
    """Modelo que esta view manipula"""
    template_name = "core/crud/list.html"
    """Nome do template utilizado para renderização do HTML"""


class ProjectDetailView(DefaultContextMixin, DetailView):
    """Django Class Based View para visualização detalhada dos dados de um projeto"""

    model = Project
    """Modelo que esta view manipula"""
    template_name = "core/crud/detail.html"
    """Nome do template utilizado para renderização do HTML"""


class ProjectDeleteView(DefaultContextMixin, DeleteView):
    """Django Class Based View para remoção de dados dos Projetos"""

    model = Project
    """Modelo que esta view manipula"""
    template_name = "core/crud/delete.html"
    """Nome do template utilizado para renderização do HTML"""
    success_url = reverse_lazy("project:project.list")
    """URL de Sucesso"""
