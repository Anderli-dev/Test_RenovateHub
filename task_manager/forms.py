from django import forms
from django.forms import ModelForm

from task_manager.models import Project, Task

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ["name"]
        
class TaskForm(ModelForm):
    project_id = forms.IntegerField(widget=forms.HiddenInput())
    
    class Meta:
        model = Task
        fields = ["name", "project_id"]