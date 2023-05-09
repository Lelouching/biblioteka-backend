from django.db import models

class Book(models.Model):
    class Meta:
        ordering = ["id"]

    category = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    year = models.PositiveSmallIntegerField()

   