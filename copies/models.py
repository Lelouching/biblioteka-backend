from django.db import models

class Copies(models.Model):
    class Meta:
        ordering = ("id",)

    amount_copy = models.IntegerField(default=1)

    book = models.ForeignKey(
        "books.Book",
        on_delete=models.CASCADE,
        related_name="copies",
    )

