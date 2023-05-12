from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import User


class UserSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'name', 'last_name', 'email', 'image', 'password')

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user



