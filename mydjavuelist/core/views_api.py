from typing import List
from django.http import JsonResponse

from ninja import Router, Form, Schema

from .service import tasks_svc

router = Router()


class TaskSchema(Schema):
    id: int
    description: str
    done: bool


class ListTasksSchema(Schema):
    tasks: List[TaskSchema]


@router.get("/tasks/list", response=ListTasksSchema)
def list_tasks(request):
    tasks = tasks_svc.list_tasks()
    return JsonResponse({"tasks": tasks})


@router.post("/tasks/add", response=TaskSchema)
def add_task(request, description: str = Form(...)):
    task = tasks_svc.add_task(request.POST["description"])
    return JsonResponse(task)
