from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# In views.py
def set_session(request):
    request.session['username'] = 'john_doe'
    return HttpResponse("Session value set.")

def get_session(request):
    username = request.session.get('username', 'Guest')
    return HttpResponse(f"Hello, {username}!")
