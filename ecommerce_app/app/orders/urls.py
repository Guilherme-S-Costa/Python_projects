from django.urls import path
from .views import OrderDetailView, CloseOrderView, PayOrderiew

app_name = 'orders'

urlpatterns = [
    path('details/<int:pk>', OrderDetailView.as_view(), name='detail'),
    path('close/', CloseOrderView.as_view(), name='close'),
    path('pay/', PayOrderiew.as_view(), name='pay'),
]
