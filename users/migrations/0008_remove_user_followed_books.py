# Generated by Django 4.2 on 2023-05-05 19:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0007_user_followed_books"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="followed_books",
        ),
    ]