
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from task_manager.forms import TaskCreateForm
from task_manager.models import Project, Task
from django.template.response import TemplateResponse
from django.views.decorators.http import require_POST

@require_POST
def task_add(request: HttpRequest):
    form = TaskCreateForm(request.POST)
    project = get_object_or_404(Project, id=request.POST.get("project_id"))
    if form.is_valid():
        task = form.save(commit=False)
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
    
def task_delete(request: HttpRequest, id: int):
    task = get_object_or_404(Task, id=id)
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