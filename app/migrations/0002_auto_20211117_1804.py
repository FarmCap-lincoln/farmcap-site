# Generated by Django 3.1.7 on 2021-11-17 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9000),
        ),
    ]
