from django.db import models
from django_countries.fields import CountryField

# Create your models here.

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
    adults = models.CharField(choices=ADULT, max_length=128, default=0)
    children = models.CharField(choices=CHILDREN, max_length=128, default=0)
    package_category = models.CharField(choices=PACKAGE_CATEGORY, max_length=128, default=1)
    payment_mode = models.CharField(choices=PAYMENT_MODE, max_length=128, default=0)

    def __str__(self):
        return self.name