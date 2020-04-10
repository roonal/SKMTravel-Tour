from datetime import datetime

from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.timezone import now

from .models import Packages, PackageActivities, PackagePlan, Destination,PackageCostInfo, PackageReview, Staff
from tourpackages.models import Blog, Booking
from django.conf import settings
from django.core.mail import send_mail

user_list = []


def index(request):

    context = {'packages': Packages.objects.all(), 'blogs': Blog.objects.filter(blog_verification=True)}
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
               'packages': Packages.objects.all(),
               'guides': Staff.objects.filter(package_guide__slug_field=slug),


               }
    return render(request, 'user/package_details_final.html', context)


