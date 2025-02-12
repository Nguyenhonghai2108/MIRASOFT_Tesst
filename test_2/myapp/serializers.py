from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

    def validate_phone(self, value):
        """Ensure phone number contains only digits and is of valid length."""
        if not value.isdigit():
            raise serializers.ValidationError("Phone number must contain only digits.")
        if len(value) < 10 or len(value) > 15:
            raise serializers.ValidationError("Phone number length must be between 10 and 15 digits.")
        return value
