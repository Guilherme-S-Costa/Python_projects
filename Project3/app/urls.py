from django.urls import path

from . import views

urlpatterns = [
    path('', views.list_tasks, name='list_tasks'),
    path('retrive/<int:pk>/', views.retrive, name='retrive'),
    path('create/', views.create, name='create'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]
 