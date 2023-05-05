from django.urls import path

from . import views


urlpatterns = [
    path("users/<int:user_id>/follow/", views.FollowBookView.as_view()),
]