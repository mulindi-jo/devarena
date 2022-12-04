from django.urls import path
from . import views

urlpatterns = [
    path('', views.developers, name='developers'),
    path('developer_id=<str:pk>/', views.developer, name='developer'),
]
