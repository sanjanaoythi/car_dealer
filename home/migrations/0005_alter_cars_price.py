# Generated by Django 4.1.1 on 2022-12-13 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_cars_remove_payment_o_id_delete_customer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='Price',
            field=models.CharField(max_length=10),
        ),
    ]
