from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Booking
from django_countries.data import COUNTRIES


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class BookingForm(forms.ModelForm):
    AIRPORT_PICKUP = (
        ('yes', 'Yes'),
        ('no', 'No')
    )

    airport_pickup = forms.ChoiceField(choices=AIRPORT_PICKUP, widget=forms.RadioSelect())
    country = forms.ChoiceField(choices=sorted(COUNTRIES.items()))

    class Meta:
        model = Booking
        fields = ('name', 'email', 'phone_number', 'address', 'country', 'airport_pickup', 'adults',
                  'children', 'package_category', 'payment_mode')

# class BookingForm(forms.Form):
#     name = forms.CharField(max_length=50)
#     email = forms.CharField(max_length=50)
#     phone_number = forms.CharField(max_length=20)
#     address = forms.CharField(max_length=50)
#
#     nations = [
#         ('nepal', 'Nepal'),
#         ('india', 'India'),
#         ('usa', 'USA'),
#     ]
#     nationality = forms.CharField( widget=forms.Select(choices=nations))
#     # nationality = forms.CharField(max_length=20)
#
#     adults = forms.IntegerField()
#     children = forms.IntegerField()
#     arrival_date = forms.DateField()
#     departure_date = forms.DateField()
#
#     CHOICES = [('Y', 'Yes'),
#                ('N', 'No')]
#
#     airport_pickup = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
#
#     airline = forms.CharField(max_length=20)
#     flight_number = forms.CharField(max_length=20)
#     arrival_time = forms.TimeField()
#     package_Category = forms.CharField(max_length=20)
#     payment_mode = forms.CharField(max_length=20)
#

# class Booking(forms.ModelForm):
#     class Meta:
#         model = BookingRequest
#         exclude = ('request_id',)
