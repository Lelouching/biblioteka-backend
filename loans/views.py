from rest_framework import generics
from .models import Loan
from users.models import User
from copies.models import Copies
from follow.models import Follow
from .serializers import LoanBookSerializer, ReturnBookSerializer
from books.permissions import MyCustomPermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from datetime import datetime, timedelta
from rest_framework.request import Request
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
import os
import dotenv


class LoanBookView(generics.CreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanBookSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [MyCustomPermission]

    def post(self, request: Request, user_id: int):
        serializer = LoanBookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = get_object_or_404(User, pk=user_id)

        if user.date_blocked is not None and user.date_blocked < datetime.now().date():
            user.date_blocked = None
            user.blocked = False
            user.save()

        if user.blocked is True:
            return Response({"error": "user is blocked"}, 403)

        loans = Loan.objects.all().filter(user=user)
        loans = LoanBookSerializer(loans, many=True)

        for loan in loans.data:
            if loan["date_devolution"] < datetime.now().strftime("%Y-%m-%d"):
                user.blocked = True
                user.save()
                return Response({"error": "user is blocked"}, 403)

        copy_id = serializer.validated_data["copy_id"]

        already_have_copy = Loan.objects.filter(copy_id=copy_id, user=user)

        if already_have_copy:
            return Response({"error": "the user already have this copy"}, 409)

        copy = get_object_or_404(Copies, pk=copy_id)

        if copy.amount_copy == 0:
            return Response({"error": "copies out of stock"}, 403)

        date_increase = datetime.now() + timedelta(days=7)

        if date_increase.isoweekday() == 6:
            date_increase += timedelta(days=2)
        elif date_increase.isoweekday() == 7:
            date_increase += timedelta(days=1)

        date_devolution = date_increase.strftime("%Y-%m-%d")

        loan = Loan.objects.create(date_devolution=date_devolution, user=user, copy=copy)

        copy.amount_copy = copy.amount_copy - 1
        copy.save()

        return Response(LoanBookSerializer(loan).data, 201)


class ReturnBookView(generics.CreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = ReturnBookSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [MyCustomPermission]

    def post(self, request: Request, user_id: int):
        serializer = ReturnBookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = get_object_or_404(User, pk=user_id)

        loan_id = serializer.validated_data["loan_id"]
        loan = get_object_or_404(Loan, pk=loan_id, user=user)

        loan.delete()

        if loan.date_devolution < datetime.now().date():
            user.blocked = True
            loans = Loan.objects.filter(user=user)

            need_return_other_book = False

            for user_loan in loans:
                if user_loan.date_devolution < datetime.now().date():
                    need_return_other_book = True
                    break

            if need_return_other_book is False:
                date_blocked = datetime.now() + timedelta(days=5)
                user.date_blocked = date_blocked.strftime("%Y-%m-%d")

            user.save()

        copy = get_object_or_404(Copies, id=loan.copy.id)
        copy.amount_copy = copy.amount_copy + 1
        copy.save()

        follow = Follow.objects.filter(book=copy.book)

        emails = []

        for following in follow:
            emails.append(following.user.email)

        if len(emails) > 0:
            send_mail(
                subject="The book you are following is now available",
                message=f"a book's copy {copy.book.title} is available to be loaned",
                from_email=os.getenv("EMAIL_HOST_USER"),
                recipient_list=emails,
            )

        return Response({"message": f"book {copy.book.title} returned with success"}, 200)
