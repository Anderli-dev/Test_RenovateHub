
import json
from django.db.models import Max
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from django.views.decorators.http import require_POST

from task_manager.forms import TaskCreateForm
from task_manager.models import Project, Task
from task_manager.utils import render_htmx_error


@require_POST
def task_add(request: HttpRequest):
    form = TaskCreateForm(request.POST)
    project = get_object_or_404(Project, id=request.POST.get("project_id"))
    
    if project.user != request.user:
        return render_htmx_error(request, "Access denied!", 403)
    
    if form.is_valid():
        task = form.save(commit=False)
        max_order = Task.objects.filter(project=project).aggregate(Max("order"))["order__max"]
        task.order = (max_order + 1) if max_order is not None else 0
        task.project = project
        task.save()
    else: 
        return render_htmx_error(request, "Wrong input data!", 403)

    return TemplateResponse(
        request,
        "_project_item_partial.html",
        {
            "project": project,
        },
    )
    
@require_POST
def task_delete(request: HttpRequest, task_id: int):
    task = get_object_or_404(Task, id=task_id)
    project = task.project

    if project.user != request.user:
        return render_htmx_error(request, "Access denied!", 403)
    
    task.delete()
    
    return TemplateResponse(
        request,
        "_project_item_partial.html",
        {
            "project": project,
        },
    )
    
@require_POST
def task_reorder(request):
    try:
        task_id = int(request.POST.get("task_id"))
        new_order = int(request.POST.get("new_order"))
    except (TypeError, ValueError):
        return render_htmx_error(request, "Incorrect data!", 400)

    task = get_object_or_404(Task, id=task_id)
    project = task.project

    if not request.user.is_authenticated or project.user != request.user:
        return render_htmx_error(request, "Access denied!", 403)
    
    if new_order < 0:
        return render_htmx_error(request, "Incorrect order!", 400)
    
    if new_order != task.order:
            # We get all the tasks of this project, except for the current one
            tasks = Task.objects.filter(project=task.project).exclude(id=task.id).order_by("order")

            updated_order = 0
            for t in tasks:
                if updated_order == new_order:
                    updated_order += 1
                t.order = updated_order
                t.save()
                updated_order += 1

            task.order = new_order
            task.save()
        
    project = get_object_or_404(Project, id=task.project.id)
    
    return TemplateResponse(
        request,
        "_project_item_partial.html",
        {
            "project": project,
        },
    )
    
def toggle_task_status(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.toggle_status()
    print(task.status)
    project = get_object_or_404(Project, id=task.project.id)
    return TemplateResponse(
        request,
        "_project_item_partial.html",
        {
            "project": project,
        },
    )