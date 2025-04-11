import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_htmx_header_required(client, user):
    client.force_login(user)
    response = client.get(reverse("modals_add_project"))
    assert "hx-request" not in response.headers 
