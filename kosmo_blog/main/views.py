from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login



# Create your views here.


def index(request):
    data = {
        'title': 'Главная страница'
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def registration(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(name, email, password)
        user.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'main/registration.html')


def login_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(username = name,password = password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/login')
    else:
        return render(request, 'main/login.html')