
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from follow.serializers import FollowSerializer
from django.shortcuts import get_object_or_404

from users.models import User
from books.models import Book


class FollowBookView(generics.CreateAPIView):
    serializer_class = FollowSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "user_id"

    
    def perform_create(self, serializer):
        user = get_object_or_404(User, id=self.kwargs["user_id"])
        book = get_object_or_404(Book,id=self.request.data["book_id"])
        if user.student:
            serializer.save(user = user, book = book)
        else:
            return Response({"error": "User is not a student"}, status=status.HTTP_400_BAD_REQUEST)