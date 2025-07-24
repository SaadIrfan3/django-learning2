from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Players

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Players
        fields = ['username']
