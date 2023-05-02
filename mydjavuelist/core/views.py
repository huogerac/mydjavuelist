# coding: utf-8

from typing import List, Optional

from django.http import JsonResponse


from ninja import Router, Form, Schema

from .service import tasks_svc


router = Router()


class TaskSchema(Schema):
    id: Optional[int]
    description: str
    done: bool = False


class ListTasksSchema(Schema):
    tasks: List[TaskSchema]




@router.post("/tasks/add", response=TaskSchema)
def add_task(request, task: TaskSchema):
    new_task = tasks_svc.add_task(task.description)

    return JsonResponse(new_task)



@router.get("/tasks/list", response=ListTasksSchema)

def list_tasks(request):
    tasks = tasks_svc.list_tasks()
    return JsonResponse({"tasks": tasks})
