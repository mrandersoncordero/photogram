"""Photogram views module."""

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime
import json

def hello(request):
    return HttpResponse('Oh, hi! Current server time is {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))


def sorted_integers(request):
    """Return a JSON with sorted integers."""

    #import pdb; pdb.set_trace()
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)

    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted successful'
    }

    #import pdb; pdb.set_trace()
    return HttpResponse(
        json.dumps(data, indent=4), 
        content_type='application/json'
    )


def say_hi(request, name, age):
    """Return a greeting"""

    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
        return HttpResponse(message)
    else:
        message = f'Hello, {name} welcome to photogram'
        return HttpResponse(message)
