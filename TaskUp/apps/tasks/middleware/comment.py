import http

from django.db.models import Q
from django.http import JsonResponse
from rest_framework.permissions import BasePermission
from ..models.comment import Comment
from ..models.task import Task


class CommentIsMyTask(BasePermission):

    def create(self, view):
        task = view.request.data['task']
        username = view.request.user.username
        return Task.objects.filter(Q(project__owners__username=username) | (Q(workers__user__username=username) & Q(id=task))).exists()

    def update_or_destroy(self, view):
        pk = view.kwargs.get('pk')
        return Comment.objects.filter(id=pk, owner=view.request.user)

    def has_permission(self, request, view):
        match view.action:
            case "create":
                return self.create(view)
            case ("update", "destroy"):
                return self.update_or_destroy(view)
            case _:
                return True

