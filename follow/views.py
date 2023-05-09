from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from follow.serializers import FollowSerializer
from follow.models import Follow
from django.shortcuts import get_object_or_404
from users.serializers import UserSerializer

from users.models import User
from books.models import Book


class FollowBookView(generics.CreateAPIView):
    serializer_class = FollowSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request: Request, book_id):
        user = User.objects.filter(username__iexact=request.user.username).first()
        book = get_object_or_404(Book, id=book_id)
        is_following = Follow.objects.filter(user=user, book=book).first()
        if is_following:
            return Response(
                {"error": "you already follow this book"},
                status=status.HTTP_409_CONFLICT,
            )

        if user.student:
            follow = Follow.objects.create(user=user, book=book)
            return Response(
                FollowSerializer(follow).data, status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {"error": "User is not a student"}, status=status.HTTP_400_BAD_REQUEST
            )
