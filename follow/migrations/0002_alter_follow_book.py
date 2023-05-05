# Generated by Django 4.2 on 2023-05-05 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0001_initial"),
        ("follow", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="follow",
            name="book",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="followed_by",
                to="books.book",
            ),
        ),
    ]
