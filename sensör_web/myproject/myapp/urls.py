from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('visualize/', views.visualize_data, name='visualize_data'),
]
