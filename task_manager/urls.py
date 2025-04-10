from task_manager.views.home import home
from django.urls import path

from task_manager.views import modals
from task_manager.views import task, project

urlpatterns = [
    path('', home, name='home'),
    path('project/<int:id>', project.get_project, name='get_project'),
    path('task-add/', task.task_add, name='task_add'),
    path('task/<int:task_id>/delete/', task.task_delete, name='task_delete'),
    path('task_reorder/', task.task_reorder, name='task_reorder'),
    path('toggle_task_status/<int:task_id>', task.toggle_task_status, name='toggle_task_status'),
    path(
        'modals-edit-task/<int:task_id>/edit/', 
        modals.edit_task, 
        name='modals_edit_task'
        ),
    path(
        'modals-add-project/', 
        modals.create_project, 
        name='modals_add_project'
        ),
    path(
        'modals-project/<int:id>/edit/', 
        modals.edit_project, 
        name='modals_edit_project'
        ),
    path(
        'modals-project/<int:id>/delete/', 
        modals.delete_project, 
        name='modals_delete_project'
        ),
]