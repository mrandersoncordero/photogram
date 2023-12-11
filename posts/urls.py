"""Posts URLs."""

# Django
from django.urls import path

# Views
from . import views

app_name = 'posts'

urlpatterns = [
    path(
        route='', 
        view=views.PostFeedView.as_view(), 
        name='feed'
    ),

    path(
        route='post/new', 
        view=views.CreatePostView.as_view(), 
        name='create_post'
    ),

    path(
        route='post/<int:pk>', 
        view=views.PostDetailView.as_view(), 
        name='detail'
    ),
]
