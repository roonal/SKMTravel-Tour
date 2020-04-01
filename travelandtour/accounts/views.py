from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import SignUpForm, BookingForm


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


def package_booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('index')
    else:
        form = BookingForm()
    return render(request, 'user/test_form.html', {'form': form})


def packages(request):
    # context = {'packages': Packages.objects.all()}
    return render(request, 'user/packages.html')


def profile_change(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'user-auth/profile_change_form.html', {'form': form})