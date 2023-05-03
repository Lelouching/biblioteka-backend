from rest_framework import generics, permissions
from .models import User
from .serializers import UserSerializer


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


class UserDetailAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user = super().get_object()
        if self.request.user.is_staff or user == self.request.user:
            return user
        else:
            raise permissions.PermissionDenied(
                "You do not have permission to update this user."
            )


class UserDeleteAPIView(generics.DestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user = super().get_object()
        if self.request.user.is_staff or user == self.request.user:
            return user
        else:
            raise permissions.PermissionDenied(
                "You do not have permission to delete this user."
            )
