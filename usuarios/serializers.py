from rest_framework import serializers
from .models import Usuarios

class InputSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8)
    firstName = serializers.CharField(source="first_name")
    lastName = serializers.CharField(source="last_name")
    pais = serializers.CharField()
    direccion = serializers.CharField(required=False)
    telefono = serializers.CharField()
    
    class Meta:
        abstract: True

class OutputSerializer(InputSerializer):
    password = None
    accessToken = serializers.CharField(source="access_token")
    refreshToken = serializers.CharField(source="refresh_token")
    