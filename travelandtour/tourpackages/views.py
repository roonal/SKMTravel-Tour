from django.shortcuts import render, redirect
from .forms import EducationalTourForm, BookingForm
from .models import AboutNepal, Blog
from home.models import Packages


# Create your views here.


def educational_tour(request):
    if request.method == "POST":
        form = EducationalTourForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('index')
    else:
        form = EducationalTourForm()
    return render(request, 'user/educational_tour.html', {'form': form})


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
    context = {'packages': Packages.objects.all()}
    return render(request, 'user/packages.html', context)


def about_nepal(request):
    context = {'aboutnepal': AboutNepal.objects.all()}
    return render(request, 'user/about_nepal.html', context)


def about_visa(request):
    return render(request, 'user/about_visa.html')


def blog(request):
    context = {'blogs': Blog.objects.all()}
    return render(request, 'user/blog.html', context)


def blog_details(request, pk):
    context = {'blogs': Blog.objects.filter(id=pk)}
    return render(request, 'user/blog_details.html', context)