"""Views do app Task."""

from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from apps.core.mixins import DefaultContextMixin
from apps.project.models import Project, Task


class TaskCreateView(DefaultContextMixin, CreateView):
    """Django Class Based View para criação de uma tarefa"""

    model = Task
    """Modelo que esta view manipula"""
    template_name = "core/crud/form.html"
    """Nome do template utilizado para renderização do HTML"""
    success_message = "Tarefa Cadastrado Com Sucesso!"
    """Mensagem de Sucesso"""
    fields = ("title", "status", "due_date", "project", "description")
    """Campos a serem manipulados"""

    def get_initial(self):
        """Obtém dados para inicialização do formulário de cadastr de uma task"""
        if "pid" in self.kwargs:
            project = Project.objects.get(pk=self.kwargs["pid"])
            return {"project": project}
        return {}

    def get_success_url(self):
        """Definie a URL de Sucesso de acordo com regras do negócio"""
        if "pid" in self.kwargs:
            return reverse_lazy(
                "project:project.detail", kwargs={"pk": self.kwargs["pid"]}
            )

        return reverse_lazy("project:task.list")


class TaskUpdateView(DefaultContextMixin, UpdateView):
    """Django Class Based View para atualização de uma tarefa"""

    model = Task
    """Modelo que esta view manipula"""
    template_name = "core/crud/form.html"
    """Nome do template utilizado para renderização do HTML"""
    success_url = reverse_lazy("project:task.list")
    """URL de Sucesso"""
    success_message = "Tarefa Atualizado Com Sucesso!"
    """Mensagem de Sucesso"""
    fields = ("title", "status", "due_date", "project", "description")
    """Campos a serem manipulados"""


class TaskListView(DefaultContextMixin, ListView):
    """Django Class Based View para listagem de tarefas"""

    model = Task
    """Modelo que esta view manipula"""
    template_name = "core/crud/list.html"
    """Nome do template utilizado para renderização do HTML"""


class TaskDetailView(DefaultContextMixin, DetailView):
    """Django Class Based View para visualização de detalhes de uma tarefa"""

    model = Task
    """Modelo que esta view manipula"""
    template_name = "core/crud/detail.html"
    """Nome do template utilizado para renderização do HTML"""


class TaskDeleteView(DefaultContextMixin, DeleteView):
    """Django Class Based View para remoção de uma tarefa"""

    model = Task
    """Modelo que esta view manipula"""
    template_name = "core/crud/delete.html"
    """Nome do template utilizado para renderização do HTML"""
    success_url = reverse_lazy("project:task.list")
    """URL de Sucesso"""


class TaskStatusUpdateView(DefaultContextMixin, View):
    """Altera o status da tarefa"""

    def get(self, *args, **kwargs):
        """Recebe o novo status da tarefa via GET e atualiza o statua da intância da tarefa"""
        task = Task.objects.get(pk=kwargs["pk"])
        task.status = kwargs["status"]
        task.save()

        # Retorna para a página que o chamou
        return redirect(self.request.META["HTTP_REFERER"])
