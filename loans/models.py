from django.db import models


class Loan(models.Model):
    date_devolution = models.DateField()
    start_loan = models.DateField(auto_now_add=True)
    copy = models.ForeignKey(
        "copies.Copies",
        on_delete=models.CASCADE,
        related_name="loans",
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="loans",
    )
