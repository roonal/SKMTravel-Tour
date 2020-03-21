# Generated by Django 2.2.5 on 2020-03-21 08:27

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20200321_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='arrival_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='booking',
            name='arrival_time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='departure_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
