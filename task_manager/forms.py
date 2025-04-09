from django import forms
from django.forms import ModelForm

from task_manager.models import Project, Task

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ["name"]
        
class TaskCreateForm(ModelForm):
    project_id = forms.IntegerField(widget=forms.HiddenInput())
    
    class Meta:
        model = Task
        fields = ["name", "project_id"]
        
class TaskEditForm(ModelForm):
    class Meta:
        model = Task
        fields = ["name", "priority", "deadline"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
            }),
            "priority": forms.Select(attrs={
                "class": "form-select"
            }),
            "deadline": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date"
            }),
        }