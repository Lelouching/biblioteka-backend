from rest_framework import serializers

from .models import Book

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ["id", "title", "author", "category", "year"]

   
    def create(self, validated_data):
        return Book.objects.create(**validated_data) 