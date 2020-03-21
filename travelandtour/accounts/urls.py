from django.urls import path
from . import views
from django.urls import include
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('', views.register, name='register'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.user_profile, name='profile'),
    path('package-booking/', views.package_booking, name="booking_form"),
    path('booking-request/', views.booking_request, name="booking-request"),
    path('packages/', views.packages, name="packages"),

    
]