# Generated by Django 4.2.2 on 2023-09-22 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='Transmission',
            field=models.CharField(default='Auto', max_length=30),
        ),
    ]
