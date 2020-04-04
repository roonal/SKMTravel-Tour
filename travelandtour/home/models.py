from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator


class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)
    address = models.CharField(max_length=50)
    established_date = models.DateField()

    def __str__(self):
        return self.name


class StaffRole(models.Model):
    role_id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.role


class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()
    join_date = models.DateField()
    salary = models.IntegerField()
    staff_img = models.ImageField(upload_to='Package_Images/')
    role_id = models.ForeignKey(StaffRole, on_delete=models.CASCADE)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class PackageType(models.Model):
    package_type_id = models.AutoField(primary_key=True)
    package_type = models.CharField(max_length=30)

    def __str__(self):
        return self.package_type


class Packages(models.Model):
    package_id = models.AutoField(primary_key=True)
    package_name = models.CharField(max_length=50)
    slug_field = models.SlugField(unique=True, null=True, blank=True)
    total_days = models.CharField(max_length=20)
    price = models.IntegerField()
    max_altitude = models.CharField(max_length=50)
    best_season = models.CharField(max_length=80)
    img = models.ImageField(upload_to='Package_Images/')
    difficulty = models.CharField(max_length=20)
    overview = models.TextField()
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    staff_id = models.ManyToManyField(Staff, default=1, null=True, blank=True)
    package_type = models.ForeignKey(PackageType, on_delete=models.CASCADE)

    # for showing particular name in the drop down menu in admin panel
    def __str__(self):
        return self.package_name

    def save(self, *args, **kwargs):
        self.slug_field = slugify(self.package_name)
        super(Packages, self).save(*args, **kwargs)


class PackageReview(models.Model):
    review_id = models.AutoField(primary_key=True)
    review_by = models.CharField(max_length=100)
    address = models.CharField(max_length=60)
    review_date = models.DateField()
    ratings = models.IntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    review = models.TextField()
    package_id = models.ForeignKey(Packages, on_delete=models.CASCADE)
    review_verification = models.BooleanField(default=False)

    def __str__(self):
        return self.review_by


COST_CHOICES = (
   ('cost_included', 'CostIncluded'),
   ('cost_excluded', 'CostExcluded')
)


class PackageCostInfo(models.Model):
    cost_id = models.AutoField(primary_key=True)
    cost_details = models.CharField(max_length=200)
    cost_type = models.CharField(choices=COST_CHOICES, max_length=128)
    package_cost = models.ManyToManyField(Packages)


class Destination(models.Model):
    destination_id = models.AutoField(primary_key=True)
    destination = models.CharField(max_length=50)
    package_destination = models.ManyToManyField(Packages)

    # for showing particular name in the drop down menu in admin panel
    def __str__(self):
        return self.destination


class PackagePlan(models.Model):
    plan_id = models.AutoField(primary_key=True)
    day = models.CharField(max_length=20)
    difficulty_level = models.CharField(max_length=50)
    travel_details = models.CharField(max_length=100)
    package_id = models.ForeignKey(Packages, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('plan_id', 'package_id'),)

    # for showing particular name in the drop down menu in admin panel
    def __str__(self):
        return self.travel_details


class Activities(models.Model):
    activities_id = models.AutoField(primary_key=True)
    activities = models.TextField()
    travel_mode = models.CharField(max_length=50)

    # for showing particular name in the drop down menu in admin panel
    def __str__(self):
        return self.activities


class PackageActivities(models.Model):
    package_activities_id = models.AutoField(primary_key=True)
    package_id = models.ForeignKey(Packages, on_delete=models.CASCADE)
    plan_id = models.ForeignKey(PackagePlan, on_delete=models.CASCADE)
    activities_id = models.ForeignKey(Activities, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('package_activities_id', 'package_id', 'plan_id', 'activities_id'),)


