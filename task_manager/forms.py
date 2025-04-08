from django.forms import ModelForm

from task_manager.models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ["name"]