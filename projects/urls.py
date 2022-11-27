from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('project_id=<str:pk>/', views.project, name='project'),
    path('create-project', views.create_project, name='create-project'),
    path('update-project_id=<str:pk>/', views.update_project, name='update-project'),
    path('delete-project_id=<str:pk>/', views.delete_project, name='delete-project'),
]
