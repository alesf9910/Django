from rest_framework.serializers import ModelSerializer
from ..models.worker import Worker

class WorkerSerializer(ModelSerializer):

    class Meta:
        model = Worker
        fields = '__all__'