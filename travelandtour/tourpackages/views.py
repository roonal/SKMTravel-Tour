import datetime

from django.conf import settings
from django.shortcuts import render, redirect
from .forms import EducationalTourForm, BookingForm, TripCustomizeForm, ReviewForm, AddBlogForm
from .models import AboutNepal, Blog, Gallery, UserRequest
from home.models import Packages
from django.contrib import messages
from django.core.paginator import Paginator
from travelandtour.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.core.mail import EmailMessage


def educational_tour(request):
    if request.method == "POST":
        form = EducationalTourForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            name = form.cleaned_data.get('name')
            organization_name = form.cleaned_data.get('organization_name')
            email_from = form.cleaned_data.get('email')
            destination = form.cleaned_data.get('destination')
            address = form.cleaned_data.get('address')

            subject = 'New Group Tour request'
            message = 'Dear admin of SKM Travel and Tour, you received a new educational/group tour request.' \
                      ' The details are as follow: ' + \
                      ' Requested By: {}, Address: {}, Organization Name: {}, Email: {}, Requested Destination: {}' \
                .format(name, address, organization_name, email_from, destination) + \
                      'Please review the group tour request and notified the user. Thank You'

            email = settings.EMAIL_HOST_USER
            recipient = [email]

            send_mail(subject, message, email_from, recipient, fail_silently=False)

            messages.success(request, 'Successfully requested for the group/education tour')
            return redirect('educational_tour')
        else:
            messages.warning(request, 'Please correct the error below.')
    else:
        form = EducationalTourForm()
    context = {'form': form, 'packages': Packages.objects.all()}
    return render(request, 'user/educational_tour.html', context)


def package_booking(request, slug):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)

            airport_pickup = form.cleaned_data.get('airport_pickup')
            if airport_pickup == 'yes':

                arrival_date = form.cleaned_data.get('arrival_date')
                departure_date = form.cleaned_data.get('departure_date')
                airport_time = form.cleaned_data.get('airport_time')

                if arrival_date is not None and departure_date is not None and airport_time is not None:
                    diff = departure_date - arrival_date
                    if arrival_date < datetime.date.today() or departure_date < arrival_date \
                            or diff.days < 5:
                        messages.warning(request,
                                         'Please Make sure about the arrival and departure date. Its incorrect.')
                        context = {'form': form, 'tourpackages': Packages.objects.filter(slug_field=slug),
                                   'packages': Packages.objects.all()}
                        return render(request, 'user/test_form.html', context)
                else:
                    messages.warning(request, 'Please inform us about the arrival date, '
                                              'departure date and airport time clearly.')
                    context = {'form': form, 'tourpackages': Packages.objects.filter(slug_field=slug),
                               'packages': Packages.objects.all()}
                    return render(request, 'user/test_form.html', context)

            post.save()

            name = form.cleaned_data.get('name')
            package_name = form.cleaned_data.get('selected_package')
            email_from = form.cleaned_data.get('email')
            country = form.cleaned_data.get('country')
            address = form.cleaned_data.get('address')

            subject = 'New tour booking request'
            message = 'Dear admin of SKM Travel and Tour, you received a new tour booking request.' \
                ' The details are as follow: ' + \
                ' Requested By: {}, Requested Package Name: {}, Email: {}, Country: {}, Address: {}'\
                .format(name, package_name, email_from, country, address) +\
                'Please review the request and notified the user. Thank You'

            email = settings.EMAIL_HOST_USER
            recipient = [email]

            send_mail(subject, message, email_from, recipient, fail_silently=False)

            messages.success(request, 'Successfully requested for the package booking')
            return redirect('booking_form', slug=slug)
        else:
            messages.warning(request, 'Please correct the error below.')
    else:
        form = BookingForm()
    context = {'form': form, 'tourpackages': Packages.objects.filter(slug_field=slug), 'packages': Packages.objects.all()}
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
    blog_list = Blog.objects.filter(blog_verification=True)
    paginator = Paginator(blog_list, 6)  # Show 6 blogs per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'blogs': page_obj, 'packages': Packages.objects.all()}
    return render(request, 'user/blog.html', context)


def blog_details(request, slug):
    context = {'blogs': Blog.objects.filter(slug_field=slug), 'packages': Packages.objects.all()}
    return render(request, 'user/blog_details.html', context)


def about_company(request):
    return render(request, 'user/about_company.html')


def company_profile(request):
    return render(request, 'user/company_profile.html')


def photo_gallery(request):
    context = {'gallery': Gallery.objects.all(), 'packages': Packages.objects.all()}
    return render(request, 'user/gallery.html', context)


def customize_trip(request, slug):
    if request.method == "POST":
        form = TripCustomizeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            trip_name = form.cleaned_data.get('name')
            full_name = form.cleaned_data.get('selected_package')
            email_from = form.cleaned_data.get('email')
            country = form.cleaned_data.get('country')
            address = form.cleaned_data.get('address')

            subject = 'New Tou Customization request'
            message = 'Dear admin of SKM Travel and Tour, you received a new tour customization request.' \
                      ' The details are as follow: ' + \
                      ' Requested By: {}, Requested Trip Name: {}, Email: {}, Country: {}, Address: {}' \
                          .format(full_name, trip_name, email_from, country, address) + \
                      'Please review the request and notified the user. Thank You'

            email = settings.EMAIL_HOST_USER
            recipient = [email]

            send_mail(subject, message, email_from, recipient, fail_silently=False)

            messages.success(request, 'Successfully requested for the trip customization')
            return redirect('customize-trip', slug=slug)
        else:
            messages.warning(request, 'Please correct the error below.')
    else:
        form = TripCustomizeForm()
    context = {'form': form, 'packages': Packages.objects.all(), 'tourpackages': Packages.objects.filter(slug_field=slug)}
    return render(request, 'user/customize_trip1.html', context)


def add_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            messages.success(request, 'Successfully requested for package review')
            return redirect('add-review')
        else:
            messages.warning(request, 'Please correct the error below.')

    else:
        form = ReviewForm()
    context = {'form': form, 'packages': Packages.objects.all()}
    return render(request, 'user/add_review.html', context)


def user_request(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')

    a = UserRequest(name=name, email=email, message=message)
    a.save()
    return redirect('index')


def add_blog(request):
    if request.method == "POST":
        form = AddBlogForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            messages.success(request, 'Successfully requested for blog post')
            return redirect('add-blog')
        else:
            messages.warning(request, 'Please correct the error below.')
    else:
        form = AddBlogForm()
    context = {'form': form, 'packages': Packages.objects.all()}
    return render(request, 'user/add_blog.html', context)