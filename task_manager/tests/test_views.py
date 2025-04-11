import pytest
from django.urls import reverse
from task_manager.models import Project, Task, User

@pytest.mark.django_db
def test_project_created_successfully(client, user):
    client.force_login(user)
    response = client.post(reverse("modals_add_project"), data={"name": "Test Project"}, HTTP_HX_REQUEST="true")
    assert response.status_code == 200
    assert Project.objects.filter(name="Test Project", user=user).exists()

@pytest.mark.django_db
def test_task_delete_success(client, user):
    client.force_login(user)
    project = Project.objects.create(user=user, name="Proj")
    task = Task.objects.create(project=project, name="ToDelete")
    response = client.post(
        reverse("task_delete", args=[task.id]),
        HTTP_HX_REQUEST="true"
    )
    assert response.status_code == 200
    assert not Task.objects.filter(id=task.id).exists()

@pytest.mark.django_db
def test_task_delete_unauthorized(client, user):
    user2 = User.objects.create_user("other", password="123")
    project = Project.objects.create(user=user2, name="Alien")
    task = Task.objects.create(project=project, name="Hidden")

    client.force_login(user)
    response = client.post(reverse("task_delete", args=[task.id]), HTTP_HX_REQUEST="true")
    assert response.status_code == 403
    
@pytest.mark.django_db
def test_edit_task_post_valid(client, user):
    client.force_login(user)
    project = Project.objects.create(user=user, name="Proj")
    task = Task.objects.create(project=project, name="Old")
    response = client.post(
        reverse("modals_edit_task", args=[task.id]),
        data={"name": "Updated", "priority": 3, "deadline": "2025-04-11"},
        HTTP_HX_REQUEST="true"
    )
    task.refresh_from_db()
    assert response.status_code == 200
    assert task.name == "Updated"
    assert task.priority == 3

@pytest.mark.django_db
def test_edit_task_post_invalid(client, user):
    client.force_login(user)
    project = Project.objects.create(user=user, name="Proj")
    task = Task.objects.create(project=project, name="Old")
    response = client.post(
        reverse("modals_edit_task", args=[task.id]),
        data={"name": "<bad>", "priority": 3, "deadline": "2025-04-11"},
        HTTP_HX_REQUEST="true"
    )
    assert response.status_code == 400
    assert b"Wrong input data" in response.content