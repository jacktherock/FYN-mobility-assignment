# Generated by Django 5.0.2 on 2024-02-21 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricingconfiguration',
            name='day_of_week',
            field=models.CharField(choices=[('Mon', 'Monday'), ('Tue', 'Tuesday'), ('Wed', 'Wednesday'), ('Thu', 'Thursday'), ('Fri', 'Friday'), ('Sat', 'Saturday'), ('Sun', 'Sunday')], default='Mon', max_length=3),
        ),
        migrations.AddField(
            model_name='pricingconfiguration',
            name='max_distance',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='pricingconfiguration',
            name='min_distance',
            field=models.FloatField(default=0.0),
        ),
    ]
