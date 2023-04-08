from django.urls import path
from . import views

app_name = 'cryptoden'

urlpatterns = [
    path('cryptoden/', views.index, name='crypto-main'),
    path('cryptoden/login/', views.userLogin, name='crypto-login'),
    path('cryptoden/logout/', views.userLogout, name='crypto-logout'),
]