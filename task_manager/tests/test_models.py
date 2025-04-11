import pytest
from task_manager.models import Project, Task

@pytest.mark.django_db
def test_project_str(user):
    project = Project.objects.create(user=user, name="My Project")
    assert str(project) == "My Project"

@pytest.mark.django_db
def test_task_str_and_toggle(user):
    project = Project.objects.create(user=user, name="Proj")
    task = Task.objects.create(project=project, name="Task 1", status=False)
    assert str(task) == "Task 1"
    task.toggle_status()
    task.refresh_from_db()
    assert task.status is True

