# Generated by Django 5.0.2 on 2024-02-23 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricing', '0009_delete_calculatedprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricingconfiguration',
            name='calculated_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
