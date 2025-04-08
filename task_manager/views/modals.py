import json

from django.http import HttpRequest, HttpResponse
from django.template.response import TemplateResponse

from task_manager.forms import CreateProjectForm

from ..utils import for_htmx


@for_htmx(use_block_from_params=True)
def create_project(request: HttpRequest):
    if request.method == "POST":
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return HttpResponse(
                headers={
                    "Hx-Trigger": json.dumps(
                        {
                            "closeModal": True,
                            "projectCreated": project.id,
                        }
                    )
                }
            )
    else:
        form = CreateProjectForm()
    return TemplateResponse(request, "modals_add_project.html", {"form": form})