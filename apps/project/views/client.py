"""Views do app Client."""

from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from apps.core.mixins import DefaultContextMixin
from apps.project.models import Client


class ClientCreateView(DefaultContextMixin, CreateView):
    """Django Class Based View para criação de Clientes"""

    model = Client
    """Modelo que esta view manipula"""
    template_name = "core/crud/form.html"
    """Nome do template utilizado para renderização do HTML"""
    success_url = reverse_lazy("project:client.list")
    """URL de Sucesso"""
    success_message = "Cliente Cadastrado Com Sucesso!"
    """Mensagem de Sucesso"""
    fields = ("name", "role", "level", "email", "description")
    """Campos a serem manipulados"""


class ClientUpdateView(DefaultContextMixin, UpdateView):
    """Django Class Based View para atualização de dados dos clientes"""

    model = Client
    """Modelo que esta view manipula"""
    template_name = "core/crud/form.html"
    """Nome do template utilizado para renderização do HTML"""
    success_url = reverse_lazy("project:client.list")
    """URL de Sucesso"""
    success_message = "Cliente Atualizado Com Sucesso!"
    """Mensagem de Sucesso"""
    fields = ("name", "role", "level", "email", "description")
    """Campos a serem manipulados"""


class ClientListView(DefaultContextMixin, ListView):
    """Django Class Based View para listagem de clientes"""

    model = Client
    """Modelo que esta view manipula"""
    template_name = "core/crud/list.html"
    """Nome do template utilizado para renderização do HTML"""


class ClientDetailView(DefaultContextMixin, DetailView):
    """Django Class Based View para visualização de detalhes de um cliente"""

    model = Client
    """Modelo que esta view manipula"""
    template_name = "core/crud/detail.html"
    """Nome do template utilizado para renderização do HTML"""


class ClientDeleteView(DefaultContextMixin, DeleteView):
    """Django Class Based View para remoção de um cliente"""

    model = Client
    """Modelo que esta view manipula"""
    template_name = "core/crud/delete.html"
    """Nome do template utilizado para renderização do HTML"""
    success_url = reverse_lazy("project:client.list")
    """Mensagem de Sucesso"""
