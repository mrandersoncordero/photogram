"""Photogram URLs module."""

# Django
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

# app
from photogram import views as local_views
from posts import views as posts_views

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    path('hello-world', local_views.hello),
    path('sorted', local_views.sorted_integers),
    path('hi/<str:name>/<int:age>', local_views.say_hi),


    path('posts', posts_views.list_posts),
]
