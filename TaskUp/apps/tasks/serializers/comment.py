from datetime import datetime

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from ..models.comment import Comment
from ...accounts.serializers import UserSerializer


class CommentSerializer(ModelSerializer):
    owner = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Comment
        exclude = ['created_date', 'update_date']

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        result = super().create(validated_data)
        result.save()
        return result

    def update(self, instance, validated_data):
        del validated_data["task"]
        result = super().update(instance, validated_data)
        result.update_date = datetime.now()
        result.save()
        return result

    def to_representation(self, instance):
        result = super().to_representation(instance)
        del result['task']
        return result

    def get_owner(self, obj):
        return UserSerializer(obj.owner).data


