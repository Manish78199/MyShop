# Generated by Django 3.2.9 on 2022-11-11 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyShop', '0009_orderupdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='orderupdate',
            name='update_time',
            field=models.DateTimeField(),
        ),
    ]
