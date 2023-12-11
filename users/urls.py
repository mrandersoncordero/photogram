"""Users URLS"""

# Django
from django.urls import path

# Views
from . import views

app_name = 'users'

urlpatterns = [
    # Management
    path(
        route='login/', 
        view=views.login_view, 
        name='login'
    ),
    path(
        route='logout/', 
        view=views.logout_view, 
        name='logout'
    ),
    path(
        route='signup/', 
        view=views.signup, 
        name='signup'
    ),
    path(
        route='me/profile', 
        view=views.update_profile, 
        name='update_profile'
    ),

    # Posts
    path(
        route='<str:username>/',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),
]
