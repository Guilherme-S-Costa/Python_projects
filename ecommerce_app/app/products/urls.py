from django.urls import path
from .views import ProductListView, ProductRetriveView, AddCartView, RemoveFromCartView, CartView, FinalizeCartView

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('<slug>/', ProductRetriveView.as_view(), name='retrive'),
    path('add', AddCartView.as_view(), name='add'),
    path('remo/<int:id>/', RemoveFromCartView.as_view(), name='remo'),
    path('car', CartView.as_view(), name='car'),
    path('finalize', FinalizeCartView.as_view(), name='finalize')
]
