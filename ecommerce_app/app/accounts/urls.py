from django.urls import path
from .views import AccountsListView, AccountsUpdateView, LoginView, LogoutView


app_name = 'accounts'

urlpatterns = [
    path('', AccountsListView.as_view(), name='list'),
    path('update', AccountsUpdateView.as_view(), name='update'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
]
