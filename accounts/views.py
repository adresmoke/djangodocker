from django.views.generic import CreateView
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'



@login_required
def home(request):
    return render(request, 'home.html', {'message': 'Привет: авторизация!'})

def public_home(request):
    return render(request, 'home.html', {'message': 'Войдите для приветствия! <a href="/accounts/login/">Логин</a>'})
