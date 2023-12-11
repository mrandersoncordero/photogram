"""Posts views module."""

# Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView

# Models
from posts.models import Post

# Forms
from posts.forms import PostForm

class PostFeedView(LoginRequiredMixin, ListView):
    """Return all published posts."""

    template_name = 'posts/feed.html'
    model = Post
    paginate_by = 5
    context_object_name = 'posts'


@login_required
def create_post(request):
    """Create new post view."""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = PostForm()

    return render(request, 'posts/new.html',{
        'form': form,
        'user': request.user,
        'profile': request.user.profile
    })