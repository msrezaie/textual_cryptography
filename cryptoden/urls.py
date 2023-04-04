from django.urls import path
from . import views

app_name = 'cryptoden'

urlpatterns = [
    path('cryptoden/', views.index, name='crypto-path'),
    path('cryptoden/login/', views.login, name='crypto-login'),
    path('cryptoden/signup/', views.signup, name='crypto-signup'),
]