import pytest
from django.urls import reverse
from task_manager.models import Project

@pytest.mark.django_db
def test_project_created_successfully(client, user):
    client.force_login(user)
    response = client.post(reverse("modals_add_project"), data={"name": "Test Project"}, HTTP_HX_REQUEST="true")
    assert response.status_code == 200
    assert Project.objects.filter(name="Test Project", user=user).exists()
