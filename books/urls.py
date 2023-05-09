from django.urls import path

from . import views


urlpatterns = [
    path("books/", views.BookView.as_view()),
    path("books/<int:pk>/", views.BookDetailView.as_view()),
    # path("albums/<int:pk>/songs/", song_views.SongView.as_view()),
]