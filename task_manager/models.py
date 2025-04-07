from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    class Priority(models.IntegerChoices):
        LOW = 1, _("Low")
        MEDIUM = 2, _("Medium")
        HIGH = 3, _("High")

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks")
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    priority = models.PositiveSmallIntegerField(
        choices=Priority.choices,
        default=Priority.MEDIUM,
    )

    class Meta:
        ordering = ["status", "priority"]
        
    def __str__(self):
        return self.name
    