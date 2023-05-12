from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from ..models.label import Label

class LabelSerializer(ModelSerializer):

    class Meta:
        model = Label
        fields = '__all__'
        
    def update(self, instance, validated_data):
        del validated_data['project']
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        result = super().to_representation(instance)
        del result['project']
        return result
