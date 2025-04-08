import json

from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse

from task_manager.forms import ProjectForm
from task_manager.models import Project

from ..utils import for_htmx


@for_htmx(use_block_from_params=True)
def create_project(request: HttpRequest):
    if request.method == "POST":
        form = ProjectForm(request.POST)
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
        form = ProjectForm()
    return TemplateResponse(request, "modals_add_project.html", {"form": form})

def edit_project(request: HttpRequest, id: int):
    project = get_object_or_404(Project,id=id)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return HttpResponse(
                headers={
                    "Hx-Trigger": json.dumps(
                        {
                            "closeModal": True,
                            "projectEdit": id,
                        }
                    )
                }
            )
    else:
        form = ProjectForm(instance=project)
    return TemplateResponse(request, "modals_edit_project.html", {"form": form})