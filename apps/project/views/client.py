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
    model = Client
    template_name = "core/crud/form.html"
    success_url = reverse_lazy("project:client.list")
    success_message = "Cliente Cadastrado Com Sucesso!"
    fields = ("name", "role", "level", "email", "description")


class ClientUpdateView(DefaultContextMixin, UpdateView):
    model = Client
    template_name = "core/crud/form.html"
    success_url = reverse_lazy("project:client.list")
    success_message = "Cliente Atualizado Com Sucesso!"
    fields = ("name", "role", "level", "email", "description")


class ClientListView(DefaultContextMixin, ListView):
    model = Client
    template_name = "core/crud/list.html"


class ClientDetailView(DefaultContextMixin, DetailView):
    model = Client
    template_name = "core/crud/detail.html"


class ClientDeleteView(DefaultContextMixin, DeleteView):
    model = Client
    template_name = "core/crud/delete.html"
    success_url = reverse_lazy("project:client.list")
