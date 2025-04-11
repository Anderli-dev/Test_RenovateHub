from django.urls import reverse
import pytest
from task_manager.forms import ProjectForm, TaskCreateForm, TaskEditForm
from task_manager.models import Project

@pytest.mark.parametrize("name, valid", [
    ("Valid name", True),
    ("<script>", False),
    (" ", False),
])
def test_project_form_validation(name, valid):
    form = ProjectForm(data={"name": name})
    assert form.is_valid() is valid

@pytest.mark.parametrize("name, valid", [
    ("Task name", True),
    ("<invalid>", False),
    ("", False),
])
def test_task_create_form_validation(name, valid):
    form = TaskCreateForm(data={"name": name, "project_id": 1})
    assert form.is_valid() == valid

def test_task_edit_form_clean_name():
    form = TaskEditForm(data={"name": "<bad>", "priority": 2, "deadline": "2025-04-11"})
    assert not form.is_valid()
    assert "HTML-теги заборонено." in str(form.errors)

@pytest.mark.django_db
def test_task_add_invalid_form(client, user):
    client.force_login(user)
    project = Project.objects.create(user=user, name="Proj")
    response = client.post(
        reverse("task_add"),
        data={"name": "<invalid>", "project_id": project.id},
        HTTP_HX_REQUEST="true"
    )
    assert response.status_code == 403
    assert b"Wrong input data" in response.content