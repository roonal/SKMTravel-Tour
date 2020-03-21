from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('educational_tour/', views.educational_tour, name="educational_tour"),
    path('package-booking/', views.package_booking, name="booking_form"),
    path('packages/', views.packages, name="packages"),

]
