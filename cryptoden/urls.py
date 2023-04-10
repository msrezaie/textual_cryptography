from django.urls import path
from . import views

app_name = 'cryptoden'

urlpatterns = [
    path('cryptoden/', views.index, name='crypto-main'),
    path('cryptoden/signin/', views.userSignin, name='crypto-signin'),
    path('cryptoden/register/', views.userRegister, name='crypto-register'),
    path('cryptoden/account/', views.userAccount, name='crypto-account'),
    path('cryptoden/logout/', views.userLogout, name='crypto-logout'),
]