from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('show_poops/', views.show_poops,name="show_poops"),
]