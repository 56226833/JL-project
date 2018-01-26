from django.shortcuts import render
from login.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            return render(request, 'main.html', {})
        else:
            return HttpResponseRedirect('/error/')

def index(request):
    return render(request, 'index.html', {})

def error(request):
    return render(request, 'error.html', {})
