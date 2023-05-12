from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from ..models.project import Project
from datetime import datetime

from ...accounts.models import User
from ...accounts.serializers import UserSerializer


class ProjectSerializer(ModelSerializer):

    owners = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)
    owner_details = serializers.SerializerMethodField()
    workers = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = '__all__'

    def get_owner_details(self, obj):
        return UserSerializer(obj.owners, many=True).data

    def create(self, validated_data):
        validated_data['status'] = False
        validated_data['owners'] = [self.context['request'].user]
        validated_data['created_date'] = str(datetime.now())
        return super().create(validated_data)

    def update(self, instance, validated_data):
        del validated_data['created_date']
        del validated_data['upload_date']
        del validated_data['status']
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        result = super().to_representation(instance)
        result.pop('owners')
        return result

    def get_workers(self, obj):
        from .worker import WorkerSerializer
        return WorkerSerializer(obj.worker_set.all(), many=True).data
