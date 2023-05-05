from rest_framework import serializers
from .models import Loan
from users.serializers import UserSerializer


class LoanSerializer(serializers.ModelSerializer):
    copy_id = serializers.IntegerField(write_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Loan
        fields = ["id", "date_devolution", "start_loan", "user", "copy_id", "copy"]
        depth = 1

        extra_kwargs = {
            "id": {"read_only": True},
            "user": {"read_only": True},
            "date_devolution": {"read_only": True},
            "start_loan": {"read_only": True},
            "copy": {"read_only": True},
        }


    def create(self, validated_data: dict):
        return Loan.objects.create(**validated_data)
