"""Testes do módulo Project."""
import datetime

from django.test import TestCase
from model_bakery import baker

from apps.core.models import Tag
from apps.project.models import Project, StatusChoices, Task


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
        print(p.tag_as_dict())

    def test_create_task(self):
        """Teste para criação de uma nova task."""
        tasks = baker.prepare("project.Task", _quantity=10)
        project: Project = baker.make(Project, tasks=tasks)
        self.assertCountEqual(project.tasks.all(), tasks)

    def test_create_subtask(self):
        """Teste para criação de uma nova subtastk."""
        task1 = baker.prepare("project.Task")
        project: Project = baker.make(Project, tasks=[task1])
        self.assertCountEqual(project.tasks.all(), [task1])

        task2: Task = baker.make("project.Task", parent=task1)
        self.assertIsNotNone(task2.parent)
        self.assertEqual(task1.title, task2.parent.title)

    def test_create_tags_in_task(self):
        tag_info = {
            "importancia": "alta",
            "natureza": "sem fins lucrativos",
            "projeto_social": "sim",
            "aceita_doacoes": "sim",
        }
        tags: list[Tag] = []
        for k, v in tag_info.items():
            tags.append(Tag.objects.create(key=k, value=v))

        Tag.objects.bulk_create(tags, ignore_conflicts=True)
        task = baker.make("project.Task", tags=tags)
        self.assertCountEqual(task.tags.all(), tags)
        for tag in task.tags.all():
            print(tag)
