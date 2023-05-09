from django.urls import path
from .views import (
    UserListAPIView,
    UserDetailAPIView,
    UserCreateAPIView,
    UserUpdateAPIView,
    UserDeleteAPIView,
    LoanListAPIView,
)
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("users/", UserListAPIView.as_view(), name="user_list"),
    path("users/create/", UserCreateAPIView.as_view(), name="user_create"),
    path("users/<int:pk>/", UserDetailAPIView.as_view(), name="user_detail"),
    path("users/<int:pk>/update/", UserUpdateAPIView.as_view(), name="user_update"),
    path("users/<int:pk>/delete/", UserDeleteAPIView.as_view(), name="user_delete"),
    path("users/login/", jwt_views.TokenObtainPairView.as_view()),
    path("users/<int:user_id>/loans", LoanListAPIView.as_view(), name="loan_list"),
]
