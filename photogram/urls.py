"""Photogram URLs module."""

# Django
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),

    path('', include(('posts.urls', 'posts'), namespace='posts')),  # Corregir aquí
    path('users/', include(('users.urls', 'users'), namespace='users')),  # Corregir aquí
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
