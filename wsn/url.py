from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('/garrysmod', name="Garry's Mod")
]