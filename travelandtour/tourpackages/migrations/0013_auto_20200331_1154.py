# Generated by Django 2.2.5 on 2020-03-31 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourpackages', '0012_booking_selected_package'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='bolg_by',
            new_name='blog_by',
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_verification',
            field=models.BooleanField(default=False),
        ),
    ]
