from rest_framework import generics
from copies.models import Copies
from books.permissions import MyCustomPermission, MyCustomPermissionDetail
from copies.serializers import CopiesSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class CopiesView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [MyCustomPermission]
    serializer_class = CopiesSerializer

    def get_queryset(self):
        book_id = self.kwargs['book_id']
        return Copies.objects.filter(book_id=book_id)

    def perform_create(self, serializer):
        book_id = self.kwargs['book_id']
        serializer.save(book_id=book_id)


class CopiesDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [MyCustomPermissionDetail]
    serializer_class = CopiesSerializer
    queryset = Copies.objects.all()
