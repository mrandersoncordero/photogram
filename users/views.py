"""Users views module."""

# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Exceptions
from django.db.utils import IntegrityError
# Models
from django.contrib.auth.models import User
from users.models import Profile

def signup(request):
    """Signup view."""
    
    if request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST['password']
        passwd_confirmation= request.POST['passwd_confirmation']

        if passwd != passwd_confirmation:
            return render(request, 'users/signup.html', {
                'error': 'Password confirmation does not match'
                })
        
        try:
            user = User.objects.create_user(username=username, password=passwd)
        except IntegrityError:
            return render(request, 'users/signup.html', {
                'error': 'Username is already in use'
                })
        
        user.first_name = request.POST['first_name']
        user.first_name = request.POST['last_name']
        user.first_name = request.POST['email']
        user.save()

        profile = Profile(user=user)
        profile.save()

        return redirect('login')
    else:
        return render(request, 'users/signup.html')

def login_view(request):
    """Login view."""

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})
    else:
        return render(request, 'users/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
    # Redirect to a success page.