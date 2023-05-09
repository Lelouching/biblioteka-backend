from rest_framework import serializers

from .models import Follow
from users.serializers import UserSerializer

class FollowSerializer(serializers.ModelSerializer):
 
    user = UserSerializer(read_only = True)
    class Meta:
        model = Follow
        fields = "__all__"
        depth = 1

    def create(self, validated_data):
        return Follow.objects.create(**validated_data)

