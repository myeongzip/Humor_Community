from django.contrib import admin
from django.urls import path,include

from tweet import views

urlpatterns = [
    path('feed', views.index),
    path('feed/create', views.todo_create),
    # path('tweet/<int:tweet_id>/', views.todo_read),
    # path('<int:twwet_id>/update/', views.todo_update),
    # path('<int:tweet_id>/delete/', views.todo_delete),

    
]