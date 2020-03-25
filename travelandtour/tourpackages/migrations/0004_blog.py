# Generated by Django 2.2.5 on 2020-03-23 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourpackages', '0003_aboutnepal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('blog_name', models.CharField(max_length=100)),
                ('bolg_by', models.CharField(max_length=50)),
                ('blog_date', models.DateField()),
                ('blog_Details', models.TextField()),
                ('img', models.ImageField(upload_to='Package_Images/')),
            ],
        ),
    ]