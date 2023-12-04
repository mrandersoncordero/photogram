"""Posts views module."""

# Django
from django.shortcuts import render
from django.http import HttpResponse

# Utilities
from datetime import datetime

posts = [
    {
        'name': 'Mont Blac',
        'user': 'Yesica Cortes',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1036',
    },
    {
        'name': 'Via Lactea',
        'user': 'C. Vander',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=903',
    },
    {
        'name': 'Nuevo auditorio',
        'user': 'Thespianartist',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1076',
    }
]

def list_posts(request):
    """Listing existing posts."""
    content = []
    for post in posts:
        content.append("""
        <p><strong>{name}</strong></p>
        <p><strong>{user} - <i>{timestamp}</i></strong></p>
        <figure><img src="{picture}"/></figure>
        """.format(**post))

    return HttpResponse('<br>'.join(content))