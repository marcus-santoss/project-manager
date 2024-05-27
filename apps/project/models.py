"""Modelos de dados do app Project."""

from django.db import models

from apps.core.models import BaseModel, Tag


class StatusChoices(models.TextChoices):  # pylint: disable=too-many-ancestors
    """Enum para os status do projeto."""

    TODO = "N", "Não Iniciado"
    DOING = "D", "Em Progresso"
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
    """Classe mínima para abstração de clientes.

    Examples:
        Criar uma instância da classe Client
        >>> from apps.project.models import Client
        >>> c:Client = Client.objects.create(
        >>> name="Jhon Wayne",
        >>> role="Developer",
        >>> level=ClientLevelChoices.SENIOR,
        >>> email="jhonwaine@acme.com",
        >>> description="Melhor dev python")
    """

    name = models.CharField(
        "Nome", null=False, blank=False, max_length=150, unique=True
    )
    role = models.CharField(
        "Cargo", null=True, blank=True, max_length=50, default="Recurso"
    )
    level = models.CharField(
        "Nível",
        blank=True,
        null=True,
        max_length=1,
        choices=ClientLevelChoices.choices,
        default=ClientLevelChoices.JUNIR,
    )
    email = models.EmailField("E-Mail", null=True, blank=True, unique=True)
    description = models.TextField("Descrição", null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Project(BaseModel):
    """
    Classe mínima para abstração de projetos

    Examples:
        Criar uma instância da classe Projet
        >>> from apps.project.models import Project
        >>> import datetime
        >>> p = Project.objects.create(
        >>> title="Test Project",
        >>> project_type=Project.ProjectType.DEVELOPMENT,
        >>> start_date=datetime.date(2024, 5, 20),
        >>> dead_line=datetime.date(2024, 7, 15),
        >>> assigned_to=Client.objects.create(name="Jhon Waine")
        >>> overview=overview)
    # Descrição dos atributos
    """

    title = models.CharField(
        "Título do Projeto", null=False, blank=False, max_length=255, unique=True
    )
    """Título do projeto"""
    start_date = models.DateField("Data Inicial", null=False, blank=False)
    """Data de inicio do projeto"""
    dead_line = models.DateField("Dead Line", null=False, blank=False)
    """Data de fim estimado do projeto"""
    overview = models.TextField("Visão Geral", null=False, blank=False)
    """Visão geral do projeto"""
    assigned_to = models.ForeignKey(
        Client,
        verbose_name="Responsável do Projeto",
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        related_name="projects",
    )
    """Responsável pelo projeto"""

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
        """Representação string do projeto"""
        return self.title


class Task(BaseModel):
    """
    Classe mínima para abstração das tasks.

    Examples:
        Criar uma instância da classe Task
        >>> from apps.project.models import Client
        >>> import datetime
        >>> t:Task = Task.objects.create(
        >>> title="Tarefa 1",
        >>> description="Implementação do scrap da página do Yahoo",
        >>> status=StatusChoices.TODO,
        >>> due_date=datetime.date(2024, 5, 20),
        >>> project=Project.objects.first()
        >>> )
    """

    title = models.CharField(
        "Título da Tarefa", null=False, blank=False, max_length=255, unique=True
    )
    """Título da tarefa"""
    description = models.TextField("Descrição", null=False, blank=False)
    """Descrição da tarefa"""
    status = models.CharField(
        "Status",
        max_length=1,
        null=False,
        blank=False,
        choices=StatusChoices,
        default=StatusChoices.TODO,
    )
    """Estatus da tarefa"""

    due_date = models.DateField("Data Estimada do Fim", null=False, blank=False)
    """Data prevista para término da tarefa"""
    project = models.ForeignKey(
        Project,
        verbose_name="Projeto",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="tasks",
    )
    """Projeto no qual esta tarefa está atrelada"""

    def __str__(self):
        """Representação string da tarefa"""
        return self.title
