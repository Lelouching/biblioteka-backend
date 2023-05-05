from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> User:
        is_superuser = validated_data.pop("is_superuser", False)

        if is_superuser:
            user = User.objects.create_superuser(**validated_data, student=False)
        else:
            user = User.objects.create_user(**validated_data)

        return user

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)

        instance.save()

        return instance

    class Meta:
        model = User
        fields = "__all__"

        read_only_fields = ["id", "date_blocked"]

        extra_kwargs = {"password": {"write_only": True}}
