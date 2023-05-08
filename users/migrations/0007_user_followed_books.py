# Generated by Django 4.2 on 2023-05-05 18:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0001_initial"),
        ("users", "0006_alter_user_is_superuser"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="followed_books",
            field=models.ManyToManyField(
                blank=True, related_name="followers", to="books.book"
            ),
        ),
    ]