from django.db.models import Q
from django.shortcuts import get_list_or_404
from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from ..middleware.label import LabelIsMyProject
from ..models.label import Label
from ..serializers import LabelSerializer


class LabelViewSet(GenericViewSet, RetrieveModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin):
    permission_classes = [LabelIsMyProject, IsAuthenticated]
    serializer_class = LabelSerializer
    queryset = Label.objects.all()

    def get_queryset(self):
        username = self.request.user.username
        return Label.objects.filter(Q(project__owners__username=username) | Q(project__worker__user__username=username)).distinct()

    def retrieve(self, request, pk=None):
        label = get_list_or_404(self.get_queryset().filter(project=pk))
        serializer = self.serializer_class(label, many=True)
        return Response(serializer.data)