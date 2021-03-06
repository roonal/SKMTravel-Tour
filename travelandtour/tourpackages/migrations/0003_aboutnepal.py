# Generated by Django 2.2.5 on 2020-03-22 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourpackages', '0002_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutNepal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('details', models.TextField()),
                ('about', models.CharField(choices=[('about_nepal', 'About Nepal Intro'), ('geography', 'Geography'), ('himalayan', 'Himalayan Region'), ('hilly', 'Hilly Region'), ('terai', 'Terai Region'), ('people', 'People'), ('religion', 'Religion'), ('history', 'History'), ('art', 'Art and Culture'), ('climate', 'Climate'), ('air', 'By Air'), ('land', 'By Land')], max_length=128)),
            ],
        ),
    ]
