from django.http import JsonResponse

from ninja import Router, Form

from .service import tasks_svc

router = Router()


@router.get("/tasks/list")
def list_tasks(request):
    tasks = tasks_svc.list_tasks()
    return JsonResponse({"tasks": tasks})


@router.post("/tasks/add")
def add_task(request, description: str = Form(...)):
    task = tasks_svc.add_task(request.POST["description"])
    return JsonResponse(task)
