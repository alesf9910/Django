from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserCreateView, UserView, UserListView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/create/', UserCreateView.as_view(), name='create user'),
    path('users/<int:pk>/', UserView.as_view(), name='actualizar, eliminar y devolver usuario'),
    path('users/', UserListView.as_view(), name='devolver usuarios')
]
