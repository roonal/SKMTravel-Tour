from django import forms
from .models import EducationalTour, Booking
from django_countries.data import COUNTRIES


class EducationalTourForm(forms.ModelForm):
    class Meta:
        model = EducationalTour
        fields = ('name', 'address', 'email', 'number', 'organization_name', 'location', 'total_people', 'destination', 'total_days')


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
