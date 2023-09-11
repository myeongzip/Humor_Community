from django.contrib import admin
from django.urls import path,include

from tweet import views

urlpatterns = [
    path('tweet/create', views.todo_create),
    path('tweet/read', views.todo_create),
    path('tweet/update', views.todo_create),
    path('tweet/delete', views.todo_create),

    
]