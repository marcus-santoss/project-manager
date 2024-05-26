"""Modelos de dados do app Project."""

from django.db import models

from apps.core.models import BaseModel, Tag


class StatusChoices(models.TextChoices):  # pylint: disable=too-many-ancestors
    """Enum para os status do projeto."""

    TODO = "N", "Não Iniciado"
    DOING = "F", "Em Progresso"
    VALIDATION = "V", "Em Validação"
    SUCCESS = "S", "Finalizado com Sucesso"
    CANCELLED = "C", "Cancelado"
    BLOCKED = "B", "Bloqueado (Aguardando)"


class ClientLevelChoices(models.TextChoices):  # pylint: disable=too-many-ancestors
    """Enum para os status do projeto."""

    SENIOR = "S", "Senior"
    PLENO = "P", "Pleno"
    JUNIR = "J", "Junior"


class Client(BaseModel):
    """Classe mínima para abstração de clientes."""

    name = models.CharField(
        "Nome", null=False, blank=False, max_length=150, unique=True
    )
    role = models.CharField(
        "Cargo", null=True, blank=True, max_length=50, default="Recurso"
    )
    level = models.CharField(
        "Nível",
        blank=False,
        null=False,
        max_length=1,
        choices=ClientLevelChoices.choices,
        default=ClientLevelChoices.JUNIR,
    )
    email = models.EmailField("E-Mail", null=False, blank=False, unique=True)
    description = models.TextField("Descrição", null=False, blank=False)

    def __str__(self) -> str:
        return self.name


class Project(BaseModel):
    """Classe mínima para abstração de projetos"""

    title = models.CharField(
        "Título do Projeto", null=False, blank=False, max_length=255, unique=True
    )
    start_date = models.DateField("Data Inicial", null=False, blank=False)
    dead_line = models.DateField("Dead Line", null=False, blank=False)
    overview = models.TextField("Visão Geral", null=False, blank=False)
    assigned_to = models.ForeignKey(
        Client,
        verbose_name="Responsável do Projeto",
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        related_name="projects",
    )

    @property
    def status(self) -> StatusChoices:
        """Determina o status do projeto baseado no status das tarefas"""

        tasks_count: int = self.tasks.count()
        todo_count: int = self.tasks.filter(status=StatusChoices.TODO).count()
        if tasks_count < 1 or todo_count == tasks_count:
            return StatusChoices.TODO

        blocked_count: int = self.tasks.filter(status=StatusChoices.BLOCKED).count()
        if blocked_count > 0:
            return StatusChoices.BLOCKED

        canceled_count: int = self.tasks.filter(status=StatusChoices.CANCELLED).count()
        if canceled_count == tasks_count:
            return StatusChoices.CANCELLED

        validation_count: int = self.tasks.filter(
            status=StatusChoices.VALIDATION
        ).count()
        if validation_count == tasks_count:
            return StatusChoices.VALIDATION

        return StatusChoices.DOING

    def __str__(self) -> str:
        return self.title


class Task(BaseModel):
    """Classe mínima para abstração das tasks."""

    title = models.CharField(
        "Título da Tarefa", null=False, blank=False, max_length=255, unique=True
    )
    description = models.TextField("Descrição", null=False, blank=False)
    status = models.CharField(
        "Status",
        max_length=1,
        null=False,
        blank=False,
        choices=StatusChoices,
        default=StatusChoices.TODO,
    )

    due_date = models.DateField("Data Estimada do Fim", null=False, blank=False)
    project = models.ForeignKey(
        Project,
        verbose_name="Projeto",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="tasks",
    )
