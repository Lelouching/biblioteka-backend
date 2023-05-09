from django.db import models

class Follow(models.Model):
    class Meta:
        ordering = ("id",)

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="follows",
    )

    book = models.ForeignKey(
        "books.Book",
        on_delete=models.CASCADE,
        related_name="followed_by",
    )

