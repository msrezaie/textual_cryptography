from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('project/<str:pk>', views.project_detail, name='project'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about')
]