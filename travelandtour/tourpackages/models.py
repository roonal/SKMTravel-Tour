import datetime

from django.db import models
from django_countries.fields import CountryField
# from home.models import Packages
from django.utils.text import slugify
from jsonschema import ValidationError

from .utils import get_unique_slug


# Create your models here.
from multiselectfield import MultiSelectField


class EducationalTour(models.Model):
    request_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)
    email = models.EmailField(max_length=100)
    number = models.CharField(max_length=20)
    organization_name = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=50)
    total_people = models.IntegerField()
    destination = models.CharField(max_length=200)
    total_days = models.IntegerField()

    def __str__(self):
        return self.name


AIRPORT_PICKUP = (
   ('yes', 'Yes'),
   ('no', 'No')
)

ADULT = (
   ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('5+', '5+')
)
CHILDREN = (
    ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('5+', '5+')
)
PACKAGE_CATEGORY = (
   ('first_class', 'First Class'),
   ('economy_class', 'Economy Class'),
    ('business_class', 'Business Class')
)
PAYMENT_MODE = (
   ('cash', 'Cash'),
   ('credit_card', 'Credit Card'),
   ('bank_transfer', 'Bank Transfer')
)


class Booking(models.Model):
    request_id = models.AutoField(primary_key=True)
    selected_package = models.CharField(max_length=100, default="abc")
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    country = CountryField()
    airport_pickup = models.CharField(choices=AIRPORT_PICKUP, max_length=128)
    arrival_date = models.DateField(null=True, blank=True)
    departure_date = models.DateField(null=True, blank=True)
    arrival_time = models.TimeField(null=True, blank=True)
    adults = models.CharField(choices=ADULT, max_length=128, default=0)
    children = models.CharField(choices=CHILDREN, max_length=128, default=0)
    package_category = models.CharField(choices=PACKAGE_CATEGORY, max_length=128, default=1)
    payment_mode = models.CharField(choices=PAYMENT_MODE, max_length=128, default=0)
    # request_package = models.ForeignKey(Packages, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


ABOUT_NEPAL = (
   ('about_nepal', 'About Nepal Intro'),
   ('geography', 'Geography'),
   ('himalayan', 'Himalayan Region'),
   ('hilly', 'Hilly Region'),
   ('terai', 'Terai Region'),
   ('people', 'People'),
   ('religion', 'Religion'),
   ('history', 'History'),
   ('art', 'Art and Culture'),
   ('climate', 'Climate'),
   ('air', 'By Air'),
   ('land', 'By Land'),


)


class AboutNepal(models.Model):
    id = models.AutoField(primary_key=True)
    details = models.TextField()
    about = models.CharField(choices=ABOUT_NEPAL, max_length=128)


class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    blog_name = models.CharField(max_length=100)
    slug_field = models.SlugField(unique=True, null=True, blank=True)
    blog_by = models.CharField(max_length=50)
    blog_date = models.DateField()
    blog_Details = models.TextField()
    img = models.ImageField(upload_to='Package_Images/')
    blog_verification = models.BooleanField(default=False)

    def __str__(self):
        return self.blog_name

    # def save(self, *args, **kwargs):
    #     self.slug_field = slugify(self.blog_name)
    #     super(Blog, self).save(*args, **kwargs)

    def save(self, *args, **kwargs):
        if not self.slug_field:
            self.slug_field = get_unique_slug(self, 'blog_name', 'slug_field')
        super().save(*args, **kwargs)


IMAGE_CATEGORY = (
   ('adventure', 'Adventure'),
   ('trekking', 'Trekking'),
   ('activities', 'Activities'),
    ('cultural', 'Cultural')
)


class Gallery(models.Model):
    id = models.AutoField(primary_key=True)
    image_category = models.CharField(choices=IMAGE_CATEGORY, max_length=128)
    img = models.ImageField(upload_to='Package_Images/')

    def __str__(self):
        return self.image_category


PACKAGE_TYPES = (
   ('tour', 'Adventure'),
   ('trekking', 'Trekking'),
   ('mountain_biking', 'Mountain Biking'),
   ('peak_climbing', 'Peak Climbing'),
    ('mountain_flights', 'Mountain Flights'),
    ('short_treks', 'Short Treks'),
    ('paragliding', 'Paragliding'),
    ('jungle_safari', 'Jungle Safari'),
    ('day_tour', 'Day Tour'),
    ('bungee_jumping', 'Bungee Jumping')
)


class CustomizeTrip(models.Model):
    id = models.AutoField(primary_key=True)
    trip_name = models.CharField(max_length=100)
    adults = models.CharField(choices=ADULT, max_length=128, default=0)
    children = models.CharField(choices=CHILDREN, max_length=128, default=0)
    budget_per_person = models.IntegerField()
    duration = models.IntegerField()
    package_type = MultiSelectField(choices=PACKAGE_TYPES)
    full_name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)
    email = models.EmailField(max_length=80)
    phone = models.CharField(max_length=50)
    country = CountryField()
    package_category = models.CharField(choices=PACKAGE_CATEGORY, max_length=128, default=1)
    payment_mode = models.CharField(choices=PAYMENT_MODE, max_length=128, default=0)
    message = models.TextField(null=True, blank=True)


class UserRequest(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=80)
    message = models.TextField(null=True, blank=True)