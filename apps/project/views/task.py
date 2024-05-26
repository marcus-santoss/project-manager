"""Views do app Task."""

from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from apps.core.mixins import DefaultContextMixin
from apps.project.models import Task


class TaskCreateView(DefaultContextMixin, CreateView):
    model = Task
    template_name = "core/crud/form.html"
    success_url = reverse_lazy("project:task.list")
    success_message = "Tarefa Cadastrado Com Sucesso!"
    fields = ("title", "status", "due_date", "project", "description")


class TaskUpdateView(DefaultContextMixin, UpdateView):
    model = Task
    template_name = "core/crud/form.html"
    success_url = reverse_lazy("project:task.list")
    success_message = "Tarefa Atualizado Com Sucesso!"
    fields = ("title", "status", "due_date", "project", "description")


class TaskListView(DefaultContextMixin, ListView):
    model = Task
    template_name = "core/crud/list.html"


class TaskDetailView(DefaultContextMixin, DetailView):
    model = Task
    template_name = "core/crud/detail.html"


class TaskDeleteView(DefaultContextMixin, DeleteView):
    model = Task
    template_name = "core/crud/delete.html"
    success_url = reverse_lazy("project:task.list")
