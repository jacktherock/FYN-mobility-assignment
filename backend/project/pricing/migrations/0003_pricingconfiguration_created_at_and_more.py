# Generated by Django 5.0.2 on 2024-02-21 14:25

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricing', '0002_pricingconfiguration_day_of_week_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='pricingconfiguration',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pricingconfiguration',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_pricing_configurations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pricingconfiguration',
            name='last_modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='pricingconfiguration',
            name='last_modified_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modified_pricing_configurations', to=settings.AUTH_USER_MODEL),
        ),
    ]
