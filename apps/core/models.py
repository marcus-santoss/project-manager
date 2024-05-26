"""Modelos de Dados do app CORE"""
import uuid

from django.db import models


class BaseModel(models.Model):
    """Modelo base para os models do sistema."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.id.hex})"

    class Meta:
        """Metaclass da classe Base."""

        ordering = ["id", "created_at", "updated_at"]
        abstract = True


class Tag(BaseModel):
    key = models.CharField("key", max_length=60, null=False, blank=False)
    value = models.CharField("value", max_length=60, null=False, blank=False)

    class Meta:
        unique_together = "key", "value"

    def __str__(self) -> str:
        return self.key + ": " + self.value
