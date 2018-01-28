from django.shortcuts import render
from login import models
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = models.Staff.objects.filter(username=username, password=password)
        if user:
            return render(request, 'main.html', {})
        else:
            return HttpResponseRedirect('/error/')

def index(request):
    return render(request, 'index.html', {})

def error(request):
    return render(request, 'error.html', {})

def registion(request):
    return render(request, 'regist.html', {})

def regist(request):
    tags = ['username','password','name','gendar','age','education','zone','qualification','dialNumber','email']
    value = {}
    if(request.method == 'POST'):
        for tag in tags:
            increment = {tag:request.POST.get(tag)}
            value.update(increment)
        models.Staff.objects.create(**value)
        return render(request, 'regist_result.html',{})
    else:
        return render(request, 'regist_fail.html',{})
