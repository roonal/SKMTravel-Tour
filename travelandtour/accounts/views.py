from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import SignUpForm


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = auth.authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
        else:
            return render(request, 'user-auth/register.html', context={"form": form})
    else:
        form = SignUpForm()
        return render(request, 'user-auth/register.html', context={"form": form})


def user_login(request):
    if request.method == 'POST':
        # request.session.get_expire_at_browser_close()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            form = AuthenticationForm(data=request.POST)
            return render(request, 'user-auth/login.html', context={"form": form})
    else:
        form = AuthenticationForm()
        return render(request, 'user-auth/login.html', context={"form": form})


def user_logout(request):
    auth.logout(request)
    return redirect('index')


def user_profile(request):
    return render(request, 'user-auth/profile.html')
