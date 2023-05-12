from django.db.models import Q
from rest_framework.permissions import BasePermission

from ..models.project import Project


class LabelIsMyProject(BasePermission):

    def create(self, view):
        project = view.request.data['project']
        username = view.request.user.username
        return Project.objects.filter(Q(owners__username=username) & Q(id=project)).exists()

    def has_permission(self, request, view):
        if view.action == 'create':
            return self.create(view)
        else:
            return True

