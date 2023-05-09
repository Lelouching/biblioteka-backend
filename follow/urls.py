from django.urls import path

from . import views


urlpatterns = [
    path("book/<int:book_id>/follow/", views.FollowBookView.as_view()),
]