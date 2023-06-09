from django.urls import path

from . import views


urlpatterns = [
    path("books/<int:book_id>/copies/", views.CopiesView.as_view()),
    path("copies/<int:pk>/", views.CopiesDetailView.as_view()),
]