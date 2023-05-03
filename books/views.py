from rest_framework import generics
from books.models import Book
from books.permissions import MyCustomPermission, MyCustomPermissionDetail
from books.serializers import BookSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class BookView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [MyCustomPermission]
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [MyCustomPermissionDetail]
    serializer_class = BookSerializer
    queryset = Book.objects.all()
