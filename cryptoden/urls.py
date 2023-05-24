from django.urls import path
from . import views

app_name = 'cryptoden'

urlpatterns = [
    path('', views.index, name='crypto-main'),
    path('signin/', views.userSignin, name='crypto-signin'),
    path('register/', views.userRegister, name='crypto-register'),
    path('account/', views.userAccount, name='crypto-account'),
    path('logout/', views.userLogout, name='crypto-logout'),
]