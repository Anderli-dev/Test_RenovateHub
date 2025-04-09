from task_manager.views.home import home
from django.urls import path

from task_manager.views.modals import create_project, delete_project, edit_project

urlpatterns = [
    path('', home, name='home'),
    path('modals-add-project/', create_project, name='modals_add_project'),
    path('modals/<int:id>/edit/', edit_project, name='modals_edit_project'),
    path('modals/<int:id>/delete/', delete_project, name='modals_delete_project'),
]