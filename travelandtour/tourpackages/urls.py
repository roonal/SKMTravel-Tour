from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('educational_tour/', views.educational_tour, name="educational_tour"),
    path('package-booking/<slug>/', views.package_booking, name="booking_form"),
    path('customize-trip/<slug>', views.customize_trip, name="customize-trip"),
    path('packages/', views.packages, name="packages"),
    path('about-nepal/', views.about_nepal, name="about-nepal"),
    path('about-visa/', views.about_visa, name="about-visa"),
    path('blog/', views.blog, name="blog"),
    path('blog-details/<slug>/', views.blog_details, name="blog-details"),
    path('about-company/', views.about_company, name="about-company"),
    path('company-profile/', views.company_profile, name="company-profile"),
    path('photo-gallery/', views.photo_gallery, name="photo-gallery"),
    path('add-review/', views.add_review, name="add-review"),
    path('user-request/', views.user_request, name="user-request"),

]
