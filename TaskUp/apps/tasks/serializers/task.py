from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from ..models.task import Task

class TaskSerializer(ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        del validated_data['status']
        del validated_data['created_date']
        return super().create(validated_data)

    def update(self, instance, validated_data):
        del validated_data['created_date']
        del validated_data['status']
        return super().update(instance, validated_data)