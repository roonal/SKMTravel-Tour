# Generated by Django 2.2.5 on 2020-04-09 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_remove_packages_staff_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='package_guide',
            field=models.ManyToManyField(blank=True, default=1, null=True, to='home.Packages'),
        ),
    ]
