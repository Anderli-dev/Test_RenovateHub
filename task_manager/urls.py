from task_manager.views.home import home
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
]