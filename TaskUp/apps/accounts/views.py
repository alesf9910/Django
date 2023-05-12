from rest_framework import permissions
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .models import User
from .serializers import UserSerializer

class UserListView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.filter(is_active=True)
    permission_classes = [permissions.IsAuthenticated]

class UserView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.filter(is_active=True)
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        self.queryset = self.queryset.filter(id=request.user.id)
        return super().update(request, args, kwargs)

    def destroy(self, request, *args, **kwargs):
        self.queryset = self.queryset.filter(id=request.user.id)
        return super().destroy(request, args, kwargs)

class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer

