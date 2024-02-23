from rest_framework import serializers
from .models import PricingConfiguration


class PricingConfigurationSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField()
    last_modified_by = serializers.SerializerMethodField()

    class Meta:
        model = PricingConfiguration
        fields = "__all__"

    def get_created_by(self, obj):
        if obj.created_by:
            return obj.created_by.username
        return None

    def get_last_modified_by(self, obj):
        if obj.last_modified_by:
            return obj.last_modified_by.username
        return None
