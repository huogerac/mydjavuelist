from mydjavuelist.accounts.models import User
from mydjavuelist.accounts.tests import fixtures
from mydjavuelist.todos.models import Task


def test_criar_task_sem_login(client):
    resp = client.post("/api/todos/tasks/add", {"new_task": "walk the dog"})
    assert resp.status_code == 401


def test_criar_task_com_login(client, db):
    fixtures.user_jon()
    client.force_login(User.objects.get(username="jon"))
    resp = client.post("/api/todos/tasks/add", {"new_task": "walk the dog"})
    assert resp.status_code == 200


def test_criar_task_com_login(client, db):
    fixtures.user_jon()
    Task.objects.create(description="walk the dog")

    client.force_login(User.objects.get(username="jon"))
    resp = client.get("/api/todos/tasks/list")
    data = resp.json()

    assert resp.status_code == 200
    assert data == {"tasks": [{"description": "walk the dog", "done": False, "id": 1}]}
