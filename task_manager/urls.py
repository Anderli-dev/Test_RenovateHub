from task_manager.views.home import home
from django.urls import path

from task_manager.views.modals import create_project

urlpatterns = [
    path('', home, name='home'),
    path('modals-add-project/', create_project, name='modals_add_project'),
]