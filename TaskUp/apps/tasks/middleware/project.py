from rest_framework import status
from rest_framework.response import Response


def iamOwnerOr401(fn):
    def wrapper(self, request, *args, **kwargs):
        username = request.user.username
        project = self.get_object()
        if not project.owners.filter(username=username).exists():
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        return fn(self, request, *args, **kwargs)
    return wrapper

