from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "main"
urlpatterns = [
    path('', views.main, name="main")
    ]