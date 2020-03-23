from django.db import models
from django_countries.fields import CountryField


# Create your models here.


class EducationalTour(models.Model):
    request_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)
    email = models.EmailField(max_length=100)
    number = models.CharField(max_length=20)
    organization_name = models.CharField(max_length=100)
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
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    country = CountryField()
    airport_pickup = models.CharField(choices=AIRPORT_PICKUP, max_length=128)
    arrival_date = models.DateField()
    departure_date = models.DateField()
    arrival_time = models.TimeField()
    adults = models.CharField(choices=ADULT, max_length=128, default=0)
    children = models.CharField(choices=CHILDREN, max_length=128, default=0)
    package_category = models.CharField(choices=PACKAGE_CATEGORY, max_length=128, default=1)
    payment_mode = models.CharField(choices=PAYMENT_MODE, max_length=128, default=0)

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
    bolg_by = models.CharField(max_length=50)
    blog_date = models.DateField()
    blog_Details = models.TextField()
    img = models.ImageField(upload_to='Package_Images/')

    def __str__(self):
        return self.blog_name

