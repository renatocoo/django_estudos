from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirecionar para a página desejada após o login
                return redirect('galeria/index.html')
    else:
        form = AuthenticationForm()
    return render(request, 'galeria/login.html', {'form': form})

from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'galeria/registro.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/home/')  # Redirecionar para a página inicial ou qualquer outra página após o logout
