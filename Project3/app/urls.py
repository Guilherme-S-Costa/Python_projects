from django.urls import path

from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('adicionar/', views.adicionar, name='adicionar'),
    path('concluir/', views.concluir, name='concluir'),
    path('deletar/', views.deletar, name='deletar'),
    path('editar/<int:pk>/', views.editar, name='editar'),
]
 