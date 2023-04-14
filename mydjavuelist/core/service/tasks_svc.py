from ..models import Task


def add_task(new_task):
    task = Task(description=new_task)
    task.save()
    return task.to_dict_json()


def list_tasks():
    tasks = Task.objects.all()
    return [item.to_dict_json() for item in tasks]