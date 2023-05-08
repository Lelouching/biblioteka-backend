from rest_framework import serializers
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "author", "category", "year"]

    # def create(self, validated_data):
    #     new_book = Book.objects.filter(title__iexact=validated_data["title"]).first()

    #     if new_book:
    #         return Response({"msg": "This book already exist."})

    #     else:
    #         return Book.objects.create(**validated_data)
