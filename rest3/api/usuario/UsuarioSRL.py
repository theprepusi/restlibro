from django.contrib.auth.models import User
from rest_framework import serializers

class UsuarioSerializado(serializers.ModelSerializer):
    username = serializers.CharField(required = False)
    email = serializers.EmailField(required = False)
    first_name = serializers.CharField(required = False)
    last_name = serializers.CharField(required = False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']