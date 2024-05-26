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
    model = Project
    template_name = "core/crud/form.html"
    success_url = reverse_lazy("project:project.list")
    success_message = "Projeto Criado com Sucesso!"
    fields = ("title", "overview", "assigned_to", "start_date", "dead_line")


class ProjectUpdateView(DefaultContextMixin, UpdateView):
    model = Project
    template_name = "core/crud/form.html"
    success_url = reverse_lazy("project:project.list")
    success_message = "Projeto Criado com Sucesso!"
    fields = ("title", "overview", "assigned_to", "start_date", "dead_line")


class ProjectListView(DefaultContextMixin, ListView):
    model = Project
    template_name = "core/crud/list.html"


class ProjectDetailView(DefaultContextMixin, DetailView):
    model = Project
    template_name = "core/crud/detail.html"


class ProjectDeleteView(DefaultContextMixin, DeleteView):
    model = Project
    template_name = "core/crud/delete.html"
    success_url = reverse_lazy("project:project.list")
