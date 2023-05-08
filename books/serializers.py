from rest_framework import serializers
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.validators import UniqueValidator


from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "author", "category", "year"]
        extra_kwargs = {
            "title": {
                "validators": [
                    UniqueValidator(
                        queryset=Book.objects.all(), message="This book already exist."
                    )
                ]
            }
        }
