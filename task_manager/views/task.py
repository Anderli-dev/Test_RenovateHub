
from django.db import transaction
from django.db.models import Max
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from django.views.decorators.http import require_POST

from task_manager.forms import TaskCreateForm
from task_manager.models import Project, Task


@require_POST
def task_add(request: HttpRequest):
    form = TaskCreateForm(request.POST)
    project = get_object_or_404(Project, id=request.POST.get("project_id"))
    if form.is_valid():
        task = form.save(commit=False)
        max_order = Task.objects.filter(project=project).aggregate(Max("order"))["order__max"]
        task.order = (max_order + 1) if max_order is not None else 0
        task.project = project
        task.save()
    else: 
        pass
        # TODO add error handler

    return TemplateResponse(
        request,
        "_project_item_partial.html",
        {
            "project": project,
        },
    )
    
def task_delete(request: HttpRequest, task_id: int):
    task = get_object_or_404(Task, id=task_id)
    project = get_object_or_404(Project, id=task.project.id)
    
    if request.method == "DELETE":
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
    task_id = int(request.POST.get("task_id"))
    new_order = int(request.POST.get("new_order"))

    task = get_object_or_404(Task, id=task_id)

    if new_order != task.order:
            # Отримуємо всі таски цього проекту, крім поточної
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