from django.db import models
from django.contrib.auth.models import User


class PricingConfiguration(models.Model):
    DAYS_OF_WEEK_CHOICES = [
        ("Monday", "Monday"),
        ("Tuesday", "Tuesday"),
        ("Wednesday", "Wednesday"),
        ("Thursday", "Thursday"),
        ("Friday", "Friday"),
        ("Saturday", "Saturday"),
        ("Sunday", "Sunday"),
    ]

    distance_base_price = models.FloatField()
    distance_additional_price = models.FloatField()
    time_multiplier_factor = models.FloatField()
    waiting_charges = models.FloatField()
    day_of_week = models.CharField(
        max_length=10, choices=DAYS_OF_WEEK_CHOICES, default="Monday"
    )
    min_distance = models.FloatField(default=0.0)
    max_distance = models.FloatField(default=0.0)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="created_pricing_configurations",
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="modified_pricing_configurations",
        null=True,
    )
    last_modified_at = models.DateTimeField(auto_now=True)
    calculated_price = models.FloatField(null=True, blank=True)