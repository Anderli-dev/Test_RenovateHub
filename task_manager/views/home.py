from django.http import HttpRequest

from task_manager.models import Project
from task_manager.utils import for_htmx
from django.template.response import TemplateResponse

@for_htmx(use_block_from_params=True)
def home(request: HttpRequest):
    if request.user.is_authenticated:
        projects = Project.objects.filter(user=request.user).prefetch_related('tasks').all().order_by('id')
    else:
        projects = []
    return TemplateResponse(request, 'home.html', {'projects': projects})