"""Photogram URLs module."""

# Django
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

# app
from photogram import views

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    path('hello-world', views.hello),
    path('sorted', views.sorted_integers),
    path('hi/<str:name>/<int:age>', views.say_hi),
]
