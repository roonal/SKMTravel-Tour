# Generated by Django 2.2.5 on 2020-03-20 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_packagereview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tourguide',
            name='guides_id',
        ),
        migrations.AlterField(
            model_name='tourguide',
            name='staff_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='home.Staff'),
        ),
    ]
