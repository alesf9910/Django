from rest_framework.serializers import ModelSerializer
from ..models.workertask import WorkerTask

class WorkerTaskSerializer(ModelSerializer):

    class Meta:
        model = WorkerTask
        fields = '__all__'