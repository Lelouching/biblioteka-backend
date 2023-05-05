from django.urls import path
from . import views


urlpatterns = [
    path("users/<int:user_id>/loan/", views.LoanBookView.as_view()),
    path("users/<int:user_id>/return/", views.ReturnBookView.as_view()),
]