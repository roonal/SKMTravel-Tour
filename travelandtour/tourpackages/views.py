from django.shortcuts import render, redirect
from .forms import EducationalTourForm, BookingForm, TripCustomizeForm
from .models import AboutNepal, Blog, Gallery
from home.models import Packages
from travelandtour.settings import EMAIL_HOST_USER
from django.core.mail import send_mail


# Create your views here.


def educational_tour(request):
    if request.method == "POST":
        form = EducationalTourForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # radio_value = request.POST.get('choice')
            # if radio_value == 'yes':
            #     post.airport_pickup = "yes"
            # else:
            #     post.airport_pickup = "no"

            post.save()
            return redirect('index')
    else:
        form = EducationalTourForm()
    context = {'form': form, 'packages': Packages.objects.all()}
    return render(request, 'user/educational_tour.html', context)


def package_booking(request, pk):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            # subject = 'Welcome to SKM Travel & Tour'
            # message = 'Hope you are enjoying your Django Tutorials'
            # recepient = str(post['email'].value())
            # send_mail(subject,
            #           message, EMAIL_HOST_USER, [recepient], fail_silently=False)
            return redirect('index')
    else:
        form = BookingForm()
    context = {'form': form, 'tourpackages': Packages.objects.filter(package_id=pk), 'packages': Packages.objects.all()}
    return render(request, 'user/test_form.html', context)


def packages(request):
    context = {'packages': Packages.objects.all()}
    return render(request, 'user/packages.html', context)


def about_nepal(request):
    context = {'aboutnepal': AboutNepal.objects.all(), 'packages': Packages.objects.all()}
    return render(request, 'user/about_nepal.html', context)


def about_visa(request):
    context = {'packages': Packages.objects.all()}
    return render(request, 'user/about_visa.html', context)


def blog(request):
    context = {'blogs': Blog.objects.all(), 'packages': Packages.objects.all()}
    return render(request, 'user/blog.html', context)


def blog_details(request, pk):
    context = {'blogs': Blog.objects.filter(id=pk), 'packages': Packages.objects.all()}
    return render(request, 'user/blog_details.html', context)


def about_company(request):
    return render(request, 'user/about_company.html')


def company_profile(request):
    return render(request, 'user/company_profile.html')


def photo_gallery(request):
    context = {'gallery': Gallery.objects.all(), 'packages': Packages.objects.all()}
    return render(request, 'user/gallery.html', context)


def customize_trip(request):
    if request.method == "POST":
        form = TripCustomizeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('index')
    else:
        form = TripCustomizeForm()
    context = {'form': form, 'packages': Packages.objects.all()}
    return render(request, 'user/customize_trip1.html', context)

