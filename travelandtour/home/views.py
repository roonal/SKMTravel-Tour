from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Packages, PackageActivities, PackagePlan, Destination,PackageCostInfo, PackageReview, Staff
from tourpackages.models import Blog


def index(request):
    context = {'packages': Packages.objects.all(), 'blogs': Blog.objects.all()}
    return render(request, 'user/index.html', context)


def package_booking(request):
    return render(request, 'user/booking_form.html')


def package_details_final(request, slug):
    context = {'tourpackages': Packages.objects.filter(slug_field=slug),
               'destination': Destination.objects.filter(package_destination__slug_field=slug),
               'package_plan': PackagePlan.objects.filter(package_id__slug_field=slug),
               'activities': PackageActivities.objects.filter(package_id__slug_field=slug),
               'cost_info': PackageCostInfo.objects.filter(package_cost__slug_field=slug),
               'review': PackageReview.objects.filter(package_id__slug_field=slug, review_verification=True),
               'packages' : Packages.objects.all()


               }
    return render(request, 'user/package_details_final.html', context)


