from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('upload', views.upload),
    path('a', views.a) #this calls views.py me def a(). this is of the form localhost:8000/a?id=xyz
]
