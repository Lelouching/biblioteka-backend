
from rest_framework import generics, status
from rest_framework.exceptions import NotFound, APIException
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from books.models import Book
from copies.models import Copies
from copies.serializers import CopiesSerializer
from books.permissions import MyCustomPermission, MyCustomPermissionDetail
from django.utils.translation import gettext_lazy


class Conflict(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = gettext_lazy('Conflict.')
    default_code = 'conflict'


class CopiesView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [MyCustomPermission]
    serializer_class = CopiesSerializer

    def get_queryset(self):
        book_id = self.kwargs['book_id']
        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            raise NotFound({"error": "This book does not exist!"})
        return Copies.objects.filter(book=book)

    def perform_create(self, serializer):
        book_id = self.kwargs['book_id']
        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            raise NotFound({"error": "This book does not exist!"})

        existing_copies = Copies.objects.filter(book=book)
        if existing_copies.exists():
            response = {"error": "This book already has a copy."}
            raise Conflict(response)
        serializer.save(book=book)


class CopiesDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [MyCustomPermissionDetail]
    serializer_class = CopiesSerializer
    queryset = Copies.objects.all()
