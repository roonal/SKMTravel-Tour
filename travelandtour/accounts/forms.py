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
        fields = ('name', 'email', 'phone_number', 'address', 'airport_pickup', 'adults',
                  'children', 'package_category', 'payment_mode')


