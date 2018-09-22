from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """
    User Serializer
    """
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        """
        Meta class
        """
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name', 'is_active', 'is_superuser')
        read_only_fields = ('id', 'is_active', 'is_superuser')
