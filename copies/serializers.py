from rest_framework import serializers

from .models import Copies
from books.serializers import BookSerializer

class CopiesSerializer(serializers.ModelSerializer):
     
    book = serializers.SerializerMethodField()
    
    def create(self, validated_data):
        return Copies.objects.create(**validated_data)
    
    class Meta:
        model = Copies
        fields = ["id", "amount_copy", "book"]

        extra_kwargs = {
            "id": {"read_only": True},
            "book": {"read_only": True}
        }
    
    def get_book(self, obj):
        serializer = BookSerializer(obj.book)
        return serializer.data
