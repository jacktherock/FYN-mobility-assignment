# Generated by Django 5.0.2 on 2024-02-21 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricing', '0006_pricingconfiguration_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalculatedPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance_travelled', models.FloatField()),
                ('total_ride_time', models.FloatField()),
                ('waiting_time', models.FloatField()),
                ('price', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
