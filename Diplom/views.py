from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .forms import LoginUserForm, RegisterUserForm
from django.views.generic import ListView, DetailView, CreateView
from . models import *


def index(request):
    return render(request, 'index.html')

def events(request):
    return render(request, 'events.html')

def base(request):
    return render(request, 'base.html')

def login(request):
    return render(request, 'login.html')

class UserRegisterView(generic.CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'
    extra_context = {'title': 'Авторизация'}


class EventView(ListView):
    model = Event
    template_name = 'posts.html'

class AddEventView(CreateView):
    model = Event
    template_name = 'events.html'
    fields = '__all__'
