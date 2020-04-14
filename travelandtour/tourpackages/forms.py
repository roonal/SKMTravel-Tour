import datetime

from django import forms
from .models import EducationalTour, Booking, CustomizeTrip, Blog
from django_countries.data import COUNTRIES
from home.models import PackageReview


        
class EducationalTourForm(forms.ModelForm):
    class Meta:
        model = EducationalTour
        fields = ('name', 'address', 'email', 'number', 'organization_name', 'location', 'total_people', 'destination', 'total_days')


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class ReviewForm(forms.ModelForm):
    class Meta:
        model = PackageReview
        help_texts = {
            'ratings': 'Please rate out of 5 (1,2,3,4 or 5)',
        }
        labels = {
            "package_id": "Select Package Name",
            "review_by": "Your Name",
            "review": "Please write your review here"
        }
        fields = ('package_id', 'review_by', 'address', 'review_date', 'ratings', 'review')
        widgets = {
            'review_date': DateInput(),
        }


class AddBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('blog_name', 'blog_by', 'blog_date', 'blog_Details', 'img')
        widgets = {
            'blog_date': DateInput(),
        }


class BookingForm(forms.ModelForm):
    AIRPORT_PICKUP = (
        ('yes', 'Yes'),
        ('no', 'No')
    )

    airport_pickup = forms.ChoiceField(choices=AIRPORT_PICKUP, widget=forms.RadioSelect())
    # country = forms.ChoiceField(choices=sorted(COUNTRIES.items()))

    class Meta:
        model = Booking
        help_texts = {
            'departure_date': 'At least 6 days more than the arrival date',
        }
        fields = ('selected_package', 'request_user', 'name', 'email', 'phone_number', 'address', 'country', 'airport_pickup', 'adults',
                  'arrival_date', 'departure_date', 'arrival_time',  'children', 'package_category', 'payment_mode')
        widgets = {
            'arrival_date': DateInput(),
            'departure_date': DateInput(),
            'arrival_time': TimeInput(),
        }


class TripCustomizeForm(forms.ModelForm):
    class Meta:
        model = CustomizeTrip
        fields = ('trip_name', 'adults', 'children',  'budget_per_person', 'duration', 'package_type', 'full_name', 'address',
                  'email', 'phone', 'country', 'package_category', 'payment_mode', 'message')


