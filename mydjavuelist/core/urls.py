from django.urls import path

from . import views

urlpatterns = [
    path("tasks/add", views.add_task),
    path("tasks/list", views.list_tasks),
]
