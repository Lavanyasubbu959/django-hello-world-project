from django.urls import path
from . import views

urlpattern = [
    path('', views.hello_world, name = 'hello_world')
]