from django.contrib import admin
from django.urls import path,include

from tweet import views

urlpatterns = [
    path('feed', views.index),
    path('feed/create', views.todo_create),
    
]