from rest_framework import serializers
from .models import LocationHistory
from phones.serializers import PhoneSerializer
from phones.models import Phone
from django.contrib.gis.geos import Point

class LocationHistorySerializer(serializers.ModelSerializer):
    phone = PhoneSerializer(read_only=True)
    phone_id = serializers.PrimaryKeyRelatedField(queryset=Phone.objects.all(), source="phone")
    class Meta:
        model = LocationHistory
        fields = (
            "id",
            "phone",
            "phone_id",
            "location",
            "battery",
            "wifi",
            "dt_creation"
        )
    
    def get_location(self, obj) -> dict:
        return {"latitude": obj.location.y, "longitude": obj.location.x}
    
    def create(self, validated_data) -> LocationHistory:
        location_data = validated_data.pop("location")
        location = Point(location_data["longitude"], location_data["latitude"])
        validated_data["location"] = location
        validated_data.pop("user", None)
        location_history = LocationHistory.objects.create(**validated_data)
        return location_history