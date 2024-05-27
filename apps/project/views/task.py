"""Views do app Task."""

from django.shortcuts import redirect

from apps.core.mixins import DefaultContextMixin
from apps.project.models import Project, Task
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)


class TaskCreateView(DefaultContextMixin, CreateView):
    model = Task
    template_name = "core/crud/form.html"
    success_message = "Tarefa Cadastrado Com Sucesso!"
    fields = ("title", "status", "due_date", "project", "description")

    def get_initial(self):
        if "pid" in self.kwargs:
            project = Project.objects.get(pk=self.kwargs["pid"])
            return {"project": project}
        return {}

    def get_success_url(self):
        if "pid" in self.kwargs:
            return reverse_lazy(
                "project:project.detail", kwargs={"pk": self.kwargs["pid"]}
            )

        return reverse_lazy("project:task.list")


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


class TaskStatusUpdateView(DefaultContextMixin, View):
    def get(self, *args, **kwargs):
        task = Task.objects.get(pk=kwargs["pk"])
        task.status = kwargs["status"]
        task.save()
        return redirect(self.request.META["HTTP_REFERER"])
