# Generated by Django 4.2.4 on 2023-08-08 19:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='phone_number',
            field=models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(message='Формат номера: \n                                          7XXXXXXXXXX (X - от 0 to 9)', regex='^7\\d{10}$')]),
        ),
    ]