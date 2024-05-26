"""Modelos de dados do app Project."""
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel, Tag


class StatusChoices(models.TextChoices):  # pylint: disable=too-many-ancestors
    """Enum para os status do projeto."""

    TODO = "T", _("Todo")
    DOING = "D", _("DOING")
    VALIDATION = "V", _("Validation")
    SUCCESS = "S", _("Success")
    CANCELLED = "C", _("Cancelled")
    BLOCKED = "B", _("Blocked")


class Squad(BaseModel):
    """Class  mínima para abstração das squads de clientes."""

    name = models.CharField(
        _("Squad Name"), null=False, blank=False, max_length=255, unique=True
    )


class Client(BaseModel):
    """Classe mínima para abstração de clientes."""

    name = models.CharField(
        _("Name"), null=False, blank=False, max_length=255, unique=True
    )
    email = models.EmailField(_("E-Mail"), null=False, blank=False, unique=True)
    squad = models.ForeignKey(
        Squad, verbose_name=_("Squad"), on_delete=models.SET_NULL, null=True
    )


class Project(BaseModel):
    """Classe mínima para abstração de projetos"""

    class ProjectType(models.TextChoices):  # pylint: disable=too-many-ancestors
        """Enum para abstração dos tipos de projeto."""

        FINANCIAL = "F", _("Financial")
        ELETRICAL = "T", _("Eletrical")
        DEVELOPMENT = "D", _("Development")
        BUSSINESS = "B", _("Business")
        MARKETING = "M", _("Marketing")

    title = models.CharField(
        _("Project Title"), null=False, blank=False, max_length=255, unique=True
    )
    status = models.CharField(
        _("Project Status"),
        max_length=1,
        null=False,
        blank=False,
        choices=StatusChoices,
        default=StatusChoices.TODO,
    )
    project_type = models.CharField(
        _("Project Type"),
        null=False,
        blank=False,
        max_length=1,
        choices=ProjectType.choices,
    )
    start_date = models.DateField(_("Start Date"), null=False, blank=False)
    dead_line = models.DateField(_("Deadline Date"), null=False, blank=False)
    overview = models.TextField(_("Overview"), null=False, blank=False)
    tags = models.ManyToManyField(Tag, verbose_name=_("Tags"), blank=True)


class Task(BaseModel):
    """Classe mínima para abstração das tasks."""

    title = models.CharField(
        _("Project Title"), null=False, blank=False, max_length=255, unique=True
    )
    description = models.TextField(_("Description"), null=False, blank=False)
    status = models.CharField(
        _("Task Status"),
        max_length=1,
        null=False,
        blank=False,
        choices=StatusChoices,
        default=StatusChoices.TODO,
    )

    due_date = models.DateField(_("Due Date"), null=False, blank=False)
    tags = models.ManyToManyField(Tag, verbose_name=_("Tags"), blank=True)
    assigned_to = models.ForeignKey(
        Client,
        verbose_name=_("Assigned To"),
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    parent = models.ForeignKey(
        "self",
        verbose_name=_("Parent Task"),
        null=True,
        blank=True,
        related_name="tasks",
        on_delete=models.PROTECT,
    )

    @property
    def subtasks(self):
        """Propiedade para consulta das subtasks de uma task"""
        return self.objects.filter(parent=self.id).order_by("title")
