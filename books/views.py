from rest_framework import generics
from books.models import Book
from books.permissions import MyCustomPermission, MyCustomPermissionDetail
from books.serializers import BookSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import Response


class BookView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [MyCustomPermission]
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def post(self, request, *args, **kwargs):
        new_book = Book.objects.filter(title__iexact=request.data.get("title")).first()

        if new_book:
            return Response({"msg": "This book already exist."})

        else:
            return super().post(request, *args, **kwargs)


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [MyCustomPermissionDetail]
    serializer_class = BookSerializer
    queryset = Book.objects.all()
