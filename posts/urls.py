

from django import views
from django.urls import path
from .import views

urlpatterns = [
    path('',views.home, name='home'),
    path('<int:id>/',views.detail, name='detail'),
   
]