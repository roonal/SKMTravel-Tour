# Generated by Django 2.2.5 on 2020-03-29 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_packages_staff_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='packages',
            name='staff_id',
        ),
    ]
