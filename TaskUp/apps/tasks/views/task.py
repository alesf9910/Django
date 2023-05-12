import datetime

from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from ..models.task import Task
from ..serializers import TaskSerializer

class TaskViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def get_queryset(self):
        username = self.request.user.username
        return Task.objects.filter(Q(project__owners__username=username) | Q(workers__user__username=username))

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if not instance.status:
            instance.status = True
            instance.upload_date = datetime.datetime.now()
            instance.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
