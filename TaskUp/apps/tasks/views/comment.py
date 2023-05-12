from django.db.models import Q
from django.shortcuts import get_list_or_404
from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from ..middleware.comment import CommentIsMyTask
from ..models.comment import Comment
from ..serializers import CommentSerializer


class CommentViewSet(GenericViewSet, RetrieveModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin):
    permission_classes = [CommentIsMyTask, IsAuthenticated]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get_queryset(self):
        username = self.request.user.username
        return Comment.objects.filter(Q(task__project__owners__username=username) | Q(task__workers__user__username=username)).distinct()

    def retrieve(self, request, pk=None):
        label = get_list_or_404(self.get_queryset().filter(task=pk))
        serializer = self.serializer_class(label, many=True)
        return Response(serializer.data)