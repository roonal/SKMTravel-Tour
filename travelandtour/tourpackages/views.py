from django.conf import settings
from django.shortcuts import render, redirect
from .forms import EducationalTourForm, BookingForm, TripCustomizeForm, ReviewForm, AddBlogForm
from .models import AboutNepal, Blog, Gallery, UserRequest
from home.models import Packages
from django.contrib import messages
from django.core.paginator import Paginator
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
            post.save()

            subject = 'New tour booking request'
            message = 'Dear admin of SKM Travel and Tour, you received a new tour booking request.' \
                      ' The details are as follow:'
            email_from = post.email
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