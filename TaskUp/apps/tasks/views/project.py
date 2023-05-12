import datetime
from django.db.models import Q
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from ..middleware.project import iamOwnerOr401
from ..models.project import Project
from ..models.worker import Worker
from ..serializers import ProjectSerializer


class ProjectViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def get_queryset(self):
        username = self.request.user.username
        return Project.objects.filter(Q(owners__username=username) | Q(worker__user__username=username)).distinct()

    @iamOwnerOr401
    def update(self, request, *args, **kwargs):
        return super().update(request, args, kwargs)

    @iamOwnerOr401
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if not instance.status:
            instance.status = True
            instance.upload_date = datetime.datetime.now()
            instance.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        project_id = response.data['id']
        workers_data = request.data.get('workers', [])
        for worker_data in workers_data:
            Worker.objects.create(
                rol=worker_data['rol'],
                user_id=worker_data['user_id'],
                project_id=project_id
            )

        return response
