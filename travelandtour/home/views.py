from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Packages, PackageActivities, PackagePlan, Destination,PackageCostInfo, PackageReview


def index(request):
    context = {'packages': Packages.objects.all()}
    return render(request, 'user/index.html', context)


def package_booking(request):
    return render(request, 'user/booking_form.html')


def package_details_final(request, pk):
    context = {'packages': Packages.objects.filter(package_id=pk),
               'destination': Destination.objects.filter(package_destination=pk),
               'package_plan': PackagePlan.objects.filter(package_id=pk),
               'activities': PackageActivities.objects.filter(package_id=pk),
               'cost_info': PackageCostInfo.objects.filter(package_cost=pk),
               'review': PackageReview.objects.filter(package_id=pk),

               }
    return render(request, 'user/package_details_final.html', context)



