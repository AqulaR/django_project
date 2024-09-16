from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/<int:project_id>/tasks/', views.project_tasks, name='project_tasks'),
]