from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import SignUpForm
from tourpackages.models import Booking
from home.models import Packages


def register(request):
    valuenext = request.POST.get('next')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = auth.authenticate(username=username, password=raw_password)
            login(request, user)
            if valuenext == "":
                return redirect('/')

            if valuenext != "":
                return redirect(valuenext)
        else:
            return render(request, 'user-auth/register.html', context={"form": form, "packages": Packages.objects.all()})
    else:
        form = SignUpForm()
        return render(request, 'user-auth/register.html', context={"form": form,  "packages": Packages.objects.all()})


def user_login(request):
    valuenext = request.POST.get('next')
    if request.method == 'POST':
        # request.session.get_expire_at_browser_close()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and valuenext == "":
            login(request, user)
            request.session['is_logged'] = True
            return redirect('/')

        if user is not None and valuenext != "":
            login(request, user)
            request.session['is_logged'] = True
            return redirect(valuenext)
        else:
            form = AuthenticationForm(data=request.POST)
            return render(request, 'user-auth/login.html', context={"form": form,  "packages": Packages.objects.all()})
    else:
        form = AuthenticationForm()
        return render(request, 'user-auth/login.html', context={"form": form,  "packages": Packages.objects.all()})


def user_logout(request):
    auth.logout(request)
    return redirect('index')


abc = []


def user_profile(request):
    userid = request.user.id
    if abc:
        for i in range(0, len(abc)):
            abc[i] = int(abc[i])
        context = {'bookings': Booking.objects.filter(user_id=userid), 'packages': Packages.objects.all(), 'list':abc}
        return render(request, 'user-auth/profile1.html', context)
    else:
        context = {'bookings': Booking.objects.filter(user_id=userid), 'packages': Packages.objects.all()}
        return render(request, 'user-auth/profile1.html', context)


def cancel_booking(request, id):
    username = request.user.username
    useremail= request.user.email
    package = Packages.objects.filter(package_id=id)
    # pn = package.package_name
    email_from = request.user.email

    subject = 'Booking Cancellation Request'
    message = 'Dear admin of SKM Travel and Tour, you received a booking cancellation request.' \
              ' The details are as follow: ' + \
              ' Requested By: {}, Email: {}' \
                  .format(username, useremail) + \
              'Please review the cancellation request. Thank You'

    email = settings.EMAIL_HOST_USER
    recipient = [email]

    send_mail(subject, message, email_from, recipient, fail_silently=False)

    messages.success(request, 'Successfully requested for the booking cancellation')
    abc.append(id)
    return redirect('profile')

