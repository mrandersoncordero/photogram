"""Users URLS"""

# Django
from django.urls import path
from django.views.generic import TemplateView

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
        view=TemplateView.as_view(template_name='users/detail.html'),
        name='detail'
    ),
]
