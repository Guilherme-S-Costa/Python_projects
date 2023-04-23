from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('cart/add-product/<int:pk>/', views.cart, name='add-cart'),
    path('cart/delete-product/<int:pk>/', views.delete, name='delete-product'),
]
