# Generated by Django 2.2.5 on 2020-04-08 17:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_auto_20200330_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='packages',
            name='best_selling_package',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='packages',
            name='featured_package',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='packagereview',
            name='ratings',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]
