# Generated by Django 4.1.1 on 2022-10-21 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('C_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('C_IMG', models.ImageField(upload_to='')),
                ('Address', models.CharField(max_length=30)),
                ('NID', models.IntegerField()),
                ('u_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('O_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Car_ID', models.IntegerField()),
                ('Cus_ID', models.IntegerField()),
                ('Date_time', models.DateTimeField()),
                ('Status', models.CharField(max_length=30)),
                ('Address', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('Pa_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Pa_type', models.CharField(max_length=30)),
                ('Pa_check', models.CharField(max_length=30)),
                ('O_ID', models.CharField(max_length=30)),
            ],
        ),
    ]
