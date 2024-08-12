from rest_framework import serializers
from .models import Phone

class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = (
            "id",
            "phone_model",
            "user"
        )
        read_only_fields = ("id", "user")

    def create(self, validated_data) -> Phone:
        user = self.context["request"].user
        validated_data.pop("user", None)
        phone = Phone.objects.create(user=user, **validated_data)
        return phone