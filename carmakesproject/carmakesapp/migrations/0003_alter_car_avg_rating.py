# Generated by Django 4.1.3 on 2022-11-09 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carmakesapp', '0002_car_avg_rating_car_rates_number_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='avg_rating',
            field=models.DecimalField(decimal_places=1, max_digits=2),
        ),
    ]