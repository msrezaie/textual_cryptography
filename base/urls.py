from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path('', views.base, name='base'),
    path('project/<str:pk>', views.project_detail, name='project'),
]