"""Testes do módulo Project."""
import datetime

from django.test import TestCase

from apps.core.models import Tag
from apps.project.models import Project, StatusChoices


class ProjectTest(TestCase):
    """TesteCase da clase Project."""

    def test_create_project(self) -> None:
        """Teste para criação de um novo projeto."""

        t1 = Tag.objects.create(key="recorrencia", value="única")
        t2 = Tag.objects.create(key="natureza", value="sem fins lucrativos")

        overview: str = "Projeto de teste para processo seletivo"
        p = Project.objects.create(
            title="Test Project",
            project_type=Project.ProjectType.DEVELOPMENT,
            start_date=datetime.date(2024, 5, 20),
            dead_line=datetime.date(2024, 7, 15),
            overview=overview,
        )

        p.tags.add(t1, t2)

        self.assertEqual(Project.objects.all().count(), 1)
        self.assertEqual(p.title, "Test Project")
        self.assertEqual(p.project_type, Project.ProjectType.DEVELOPMENT)
        self.assertEqual(p.start_date, datetime.date(2024, 5, 20))
        self.assertEqual(p.dead_line, datetime.date(2024, 7, 15))
        self.assertEqual(p.overview, overview)
        self.assertEqual(p.status, StatusChoices.TODO)
        self.assertEqual(p.tags.count(), 2)

    def test_create_task(self):
        """Teste para criação de uma nova task."""
        self.fail()

    def test_create_subtask(self):
        """Teste para criação de uma nova subtastk."""
        self.fail()
