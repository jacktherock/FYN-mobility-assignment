from django.contrib import admin
from django.utils import timezone
from .models import PricingConfiguration


@admin.register(PricingConfiguration)
class PricingConfigurationAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "distance_base_price",
        "distance_additional_price",
        "time_multiplier_factor",
        "waiting_charges",
        "day_of_week",
        "min_distance",
        "max_distance",
        "created_by",
        "created_at",
        "last_modified_by",
        "last_modified_at",
        "calculated_price",
    ]

    def save_model(self, request, obj, form, change):
        if change:
            # Record who changed the configuration and when
            obj.last_modified_by = request.user
            obj.last_modified_at = timezone.now()
        else:
            # Record who created the configuration and when
            obj.created_by = request.user
            obj.created_at = timezone.now()

        # Calculate and save the price whenever a new configuration is added or updated
        obj.calculated_price = (
            obj.distance_base_price + (obj.min_distance * obj.distance_additional_price)
        ) + (obj.time_multiplier_factor * obj.waiting_charges)

        super().save_model(request, obj, form, change)
