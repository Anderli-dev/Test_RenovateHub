from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from task_manager.models import Project
from django.template.response import TemplateResponse

def get_project(request: HttpRequest, id: int):
    project = get_object_or_404(Project, id=id)

    return TemplateResponse(
        request,
        "_project_item_partial.html",
        {
            "project": project,
        },
    )