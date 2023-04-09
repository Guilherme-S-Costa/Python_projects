from django.urls import path

from . import views

urlpatterns = [
    path('', views.listar, name='listar'),
    path('recuperar/<int:pk>/', views.recuperar, name='recuperar'),
    path('adicionar/', views.adicionar, name='adicionar'),
    path('atualizar/<int:pk>/', views.atualizar, name='atualizar'),
    path('deletar/<int:pk>/', views.deletar, name='deletar'),
]
 