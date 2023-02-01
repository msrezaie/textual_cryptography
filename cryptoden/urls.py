from django.urls import path
from . import views

app_name = 'cryptoden'

urlpatterns = [
    path('cryptoden/', views.index, name='crypto-path'),
]