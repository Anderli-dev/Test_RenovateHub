from django.forms import ModelForm

from task_manager.models import Project

class CreateProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ["name"]