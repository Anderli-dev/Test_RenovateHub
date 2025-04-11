import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_create_project_denied_for_anonymous(client):
    response = client.get(reverse("modals_add_project"))
    assert response.status_code == 302
