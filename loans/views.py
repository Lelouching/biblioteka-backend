from rest_framework import generics
from .models import Loan
from users.models import User
from copies.models import Copies
from .serializers import LoanSerializer
from books.permissions import MyCustomPermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from datetime import datetime, timedelta


class LoanBookView(generics.CreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    lookup_url_kwarg = "user_id"

    authentication_classes = [JWTAuthentication]
    permission_classes = [MyCustomPermission]

    def perform_create(self, serializer):
        user_id = self.kwargs['user_id']
        user = get_object_or_404(User, pk=user_id)

        copy_id = self.request.data["copy_id"]
        copy = get_object_or_404(Copies, pk=copy_id)

        date_increase = datetime.now() + timedelta(days=7)

        if date_increase.isoweekday() == 6:
            date_increase += timedelta(days=2)
        elif date_increase.isoweekday() == 7:
            date_increase += timedelta(days=1)

        date_devolution = date_increase.strftime("%Y-%m-%d")

        serializer.save(user=user, copy=copy, date_devolution=date_devolution)


class ReturnBookView(generics.CreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    lookup_url_kwarg = "user_id"

    authentication_classes = [JWTAuthentication]
    permission_classes = [MyCustomPermission]

    def perform_create(self, serializer):
        user_id = self.kwargs['user_id']
        user = get_object_or_404(User, pk=user_id)
        serializer.save()
