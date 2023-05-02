from rest_framework.generics import CreateAPIView
from .serializers import UserSerializer
from .models import User


class UserView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
