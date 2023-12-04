"""Photogram views module."""

# Django
from django.http import HttpResponse

def hello(request):
    return HttpResponse('hello world')