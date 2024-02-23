from django.urls import path
from .views import PricingConfigurationViewSet

urlpatterns = [
    path(
        "pricing_config/",
        PricingConfigurationViewSet.as_view(),
        name="pricing_config",
    ),
]
