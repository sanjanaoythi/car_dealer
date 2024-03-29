# Generated by Django 4.2.2 on 2023-09-17 04:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0005_alter_cars_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='rentcars',
            fields=[
                ('Car_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Type', models.CharField(max_length=30)),
                ('Brand', models.CharField(max_length=30)),
                ('Status', models.CharField(max_length=30)),
                ('Model', models.CharField(max_length=30)),
                ('Engine', models.CharField(max_length=30)),
                ('picture', models.ImageField(upload_to='')),
                ('fare', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='rental',
            fields=[
                ('R_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Date_time', models.DateTimeField()),
                ('Rent_hour', models.CharField(max_length=30)),
                ('Rent_fare', models.CharField(max_length=30)),
                ('Car_ID', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='home.cars')),
                ('id', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
