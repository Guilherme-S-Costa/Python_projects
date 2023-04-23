from django.urls import path 
from .import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup-user'),
    path('validate_signup/', views.validate_signup, name='validate-signup'),
    path('validate_login/', views.validate_login, name='validate-login'),
    path('logout/', views.logout, name='logout'),
]

