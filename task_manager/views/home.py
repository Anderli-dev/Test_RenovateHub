from django.http import HttpRequest

from task_manager.models import Project
from task_manager.utils import for_htmx
from django.template.response import TemplateResponse

@for_htmx(use_block_from_params=True)
def home(request: HttpRequest):
    projects = Project.objects.prefetch_related('tasks').all()
    return TemplateResponse(request, 'home.html', {'projects': projects})