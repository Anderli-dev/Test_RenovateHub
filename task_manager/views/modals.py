import json

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from django.views.decorators.http import require_http_methods

from task_manager.forms import ProjectForm, TaskEditForm
from task_manager.models import Project, Task

from task_manager.utils import for_htmx, render_htmx_error


@require_http_methods(["GET", "POST"])
@login_required 
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
                            "projectChanged": project.id,
                        }
                    )
                }
            )
        else: 
            return render_htmx_error(request, "Wrong input data!", 400)
    else:
        form = ProjectForm()
    return TemplateResponse(request, "elements/modals/modals_add_project.html", {"form": form})

@require_http_methods(["GET", "POST"])
@login_required
def edit_project(request: HttpRequest, id: int):
    project = get_object_or_404(Project, id=id)
    if project.user != request.user:
        return render_htmx_error(request, "Access denied!", 403)
    
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return HttpResponse(
                headers={
                    "Hx-Trigger": json.dumps(
                        {
                            "closeModal": True,
                            "projectChanged": id,
                        }
                    )
                }
            )
        else: 
            return render_htmx_error(request, "Wrong input data!", 400)
    else:
        form = ProjectForm(instance=project)
    return TemplateResponse(request, "elements/modals/modals_edit_project.html", {"form": form})

@require_http_methods(["GET", "POST"])
@login_required 
def delete_project(request: HttpRequest, id: int):
    project = get_object_or_404(Project, id=id)
    
    if project.user != request.user:
        return render_htmx_error(request, "Access denied!", 403)
    
    if request.method == "POST":
        project.delete()
        return HttpResponse(
            headers={
                "Hx-Trigger": json.dumps(
                    {
                        "closeModal": True,
                        "projectChanged": id,
                    }
                )
            }
        )

    return TemplateResponse(request, "elements/modals/modals_delete_project.html")

@require_http_methods(["GET", "POST"])
@login_required 
def edit_task(request: HttpRequest, task_id: int):
    task = get_object_or_404(Task, id=task_id)
    project = task.project
    print(project.user, request.user)
    if project.user != request.user:
        return render_htmx_error(request, "Access denied!", 403)
    
    if request.method == "POST":
        form = TaskEditForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return HttpResponse(
                headers={
                    "Hx-Trigger": json.dumps(
                        {
                            "closeModal": True,
                            "taskChanged": task_id,
                        }
                    )
                }
            )
        else: 
            return render_htmx_error(request, "Wrong input data!", 400)
    else:
        form = TaskEditForm(instance=task)
    return TemplateResponse(request, "elements/modals/modals_edit_task.html", {"form": form})