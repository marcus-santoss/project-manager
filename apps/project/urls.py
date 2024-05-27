"""URLS do app project"""

from django.urls import path

from apps.project.views import client, project, task

app_name: str = "project"

urlpatterns: list = [
    path("list/", project.ProjectListView.as_view(), name="project.list"),
    path("create/", project.ProjectCreateView.as_view(), name="project.create"),
    path(
        "update/<uuid:pk>/", project.ProjectUpdateView.as_view(), name="project.update"
    ),
    path(
        "detail/<uuid:pk>/", project.ProjectDetailView.as_view(), name="project.detail"
    ),
    path(
        "delete/<uuid:pk>/", project.ProjectDeleteView.as_view(), name="project.delete"
    ),
    path(
        "<uuid:pid>/task/create/",
        task.TaskCreateView.as_view(),
        name="project.create_task",
    ),
    path("client/list/", client.ClientListView.as_view(), name="client.list"),
    path("client/create/", client.ClientCreateView.as_view(), name="client.create"),
    path(
        "client/update/<uuid:pk>/",
        client.ClientUpdateView.as_view(),
        name="client.update",
    ),
    path(
        "client/detail/<uuid:pk>/",
        client.ClientDetailView.as_view(),
        name="client.detail",
    ),
    path(
        "client/delete/<uuid:pk>/",
        client.ClientDeleteView.as_view(),
        name="client.delete",
    ),
    path("task/list/", task.TaskListView.as_view(), name="task.list"),
    path("task/create/", task.TaskCreateView.as_view(), name="task.create"),
    path("task/update/<uuid:pk>/", task.TaskUpdateView.as_view(), name="task.update"),
    path("task/detail/<uuid:pk>/", task.TaskDetailView.as_view(), name="task.detail"),
    path("task/delete/<uuid:pk>/", task.TaskDeleteView.as_view(), name="task.delete"),
    path(
        "task/set-status/<uuid:pk>/<str:status>/",
        task.TaskStatusUpdateView.as_view(),
        name="task.set_status",
    ),
]
