from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import SignUpForm,BookingForm


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
    # return render(request, 'user/booking_form.html')
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('index')
    else:
        form = BookingForm()
    return render(request, 'user/test_form.html', {'form': form})


def booking_request(request):
    # if request.method == 'POST':

        # req = Booking(request.POST)
        # req.save()

        # if req.is_valid():

        name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('number')
        address = request.POST.get('address')
        arrival_date = request.POST.get('arrival_date')
        departure_date = request.POST.get('departure_date')

        airport_pickup = request.POST.get('pickup')
        # airport_pickup = req.cleaned_data.get('CHOICES')
        # airport_pickup = dict(req.fields['airport_pickup'].choices)[airport_pickup]

        airline = request.POST.get('airline')
        flight_number = request.POST.get('flight_number')
        arrival_time = request.POST.get('arrival_time')
        nationality = request.POST.get('nationality')
        adults = request.POST.get('adults')
        children = request.POST.get('children')
        package_category = request.POST.get('package_category')
        payment_mode = request.POST.get('payment_mode')

        # a = BookingRequest(name=name, email=email,phone_number=phone_number,address=address,arrival_date=arrival_date,
        #                    departure_date=departure_date, airport_pickup=airport_pickup, airline=airline,
        #                    flight_number=flight_number, package_Category=package_category,
        #                    arrival_time=arrival_time, nationality=nationality,adults=adults, children=children,
        #                    payment_mode=payment_mode)
        # a.save()

        return render(request, 'user/form_test.html', context={"name": name, "nationality": nationality,
                                                               "airport_pickup": airport_pickup,
                                                               "arrival_date": arrival_date,
                                                               "adults": adults,
                                                               "children": children,
                                                               "payment_mode": payment_mode,
                                                               "package_category": package_category})


        #     req.save()
        #     return redirect('/')
        # else:
        #     return render(request, 'user/booking_form.html')


    # else:
    #     return render(request, 'user/booking_form.html')


def packages(request):
    # context = {'packages': Packages.objects.all()}
    return render(request, 'user/packages.html')