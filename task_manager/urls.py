from task_manager.views.home import home
from django.urls import path

from task_manager.views import modals
from task_manager.views import task, project

urlpatterns = [
    path('', home, name='home'),
    path('project/<int:id>', project.get_project, name='get_project'),
    path('task-add/', task.task_add, name='task_add'),
    path('task/<int:id>/delete/', task.task_delete, name='task_delete'),
    path(
        'modals_edit_task/<int:id>/edit/', 
        modals.edit_task, 
        name='modals_edit_task'
        ),
    path(
        'modals-add-project/', 
        modals.create_project, 
        name='modals_add_project'
        ),
    path(
        'modals-edit-project/<int:id>/edit/', 
        modals.edit_project, 
        name='modals_edit_project'
        ),
    path(
        'modals-delete-project/<int:id>/delete/', 
        modals.delete_project, 
        name='modals_delete_project'
        ),
]