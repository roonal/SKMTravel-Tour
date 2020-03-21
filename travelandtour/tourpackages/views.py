from django.shortcuts import render, redirect
from .forms import EducationalTourForm, BookingForm

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
    return render(request, 'user/packages.html')