# Generated by Django 5.0.2 on 2024-02-21 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pricing', '0007_calculatedprice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pricingconfiguration',
            name='enabled',
        ),
    ]
