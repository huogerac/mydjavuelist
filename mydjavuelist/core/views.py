# coding: utf-8
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ..commons.django_views_utils import ajax_login_required
from .service import tasks_svc


@csrf_exempt
@ajax_login_required
def add_task(request):
    task = tasks_svc.add_task(request.POST["description"])
    return JsonResponse(task)


@ajax_login_required
def list_tasks(request):
    tasks = tasks_svc.list_tasks()
    return JsonResponse({"tasks": tasks})
