# Generated by Django 2.2.5 on 2020-03-18 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staff_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('join_date', models.DateField()),
                ('salary', models.IntegerField()),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Company')),
            ],
        ),
        migrations.CreateModel(
            name='StaffRole',
            fields=[
                ('role_id', models.AutoField(primary_key=True, serialize=False)),
                ('role', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TourGuide',
            fields=[
                ('guides_id', models.AutoField(primary_key=True, serialize=False)),
                ('license_no', models.CharField(max_length=50)),
                ('experience', models.CharField(max_length=20)),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Staff')),
            ],
        ),
        migrations.AddField(
            model_name='staff',
            name='role_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.StaffRole'),
        ),
    ]
