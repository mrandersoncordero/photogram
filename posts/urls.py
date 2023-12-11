"""Posts URLs."""

# Django
from django.urls import path

# Views
from . import views

app_name = 'posts'

urlpatterns = [
    path(
        route='', 
        view=views.list_posts, 
        name='feed'
    ),

    path(
        route='new', 
        view=views.create_post, 
        name='create_post'
    ),
]