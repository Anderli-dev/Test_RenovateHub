import pytest
from django.urls import reverse

from task_manager.models import Project, Task

@pytest.mark.django_db
def test_htmx_header_required(client, user):
    client.force_login(user)
    response = client.get(reverse("modals_add_project"))
    assert "hx-request" not in response.headers 

@pytest.mark.django_db
def test_htmx_trigger_header_present(client, user):
    client.force_login(user)
    response = client.post(
        reverse("modals_add_project"),
        data={"name": "HTMX test"},
        HTTP_HX_REQUEST="true"
    )
    assert response.status_code == 200
    assert "Hx-Trigger" in response.headers

@pytest.mark.django_db
def test_task_add_correct_order(client, user):
    client.force_login(user)
    project = Project.objects.create(user=user, name="Proj")
    Task.objects.create(project=project, name="Old", order=0)

    response = client.post(
        reverse("task_add"),
        data={"name": "New", "project_id": project.id},
        HTTP_HX_REQUEST="true"
    )
    assert response.status_code == 200
    assert Task.objects.filter(name="New", project=project).exists()
    
@pytest.mark.django_db
def test_task_reorder_changes_order(client, user):
    client.force_login(user)
    project = Project.objects.create(user=user, name="Test")
    t1 = Task.objects.create(project=project, name="T1", order=0)
    t2 = Task.objects.create(project=project, name="T2", order=1)

    response = client.post(
        reverse("task_reorder"),
        data={"task_id": t2.id, "new_order": 0},
        HTTP_HX_REQUEST="true"
    )
    t1.refresh_from_db()
    t2.refresh_from_db()
    assert response.status_code == 200
    assert t1.order == 1
    assert t2.order == 0

@pytest.mark.django_db
def test_task_reorder_same_order(client, user):
    client.force_login(user)
    project = Project.objects.create(user=user, name="Project")
    task = Task.objects.create(project=project, name="Task", order=1)

    response = client.post(
        reverse("task_reorder"),
        data={"task_id": task.id, "new_order": 1},
        HTTP_HX_REQUEST="true"
    )
    task.refresh_from_db()
    assert response.status_code == 200
    assert task.order == 1

@pytest.mark.django_db
def test_task_reorder_negative_order(client, user):
    client.force_login(user)
    project = Project.objects.create(user=user, name="Project")
    task = Task.objects.create(project=project, name="Task", order=0)

    response = client.post(
        reverse("task_reorder"),
        data={"task_id": task.id, "new_order": -1},
        HTTP_HX_REQUEST="true"
    )
    assert response.status_code == 400
    assert b"Incorrect order!" in response.content