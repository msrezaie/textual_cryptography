from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('project/<str:pk>', views.project_detail, name='project'),
    path('portfolio', views.portfolio, name='portfolio')
]