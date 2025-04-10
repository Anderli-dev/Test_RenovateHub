from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from task_manager.models import Project
import json

from task_manager.utils import render_htmx_error


@login_required
def get_project(request: HttpRequest, project_id: int):
    project = get_object_or_404(Project, id=project_id)
    
    if project.user != request.user:
        return render_htmx_error(request, "Access denied!", 403)
    
    return TemplateResponse(
        request,
        "_project_item_partial.html",
        {
            "project": project,
        },
    )