# Generated by Django 4.2 on 2023-05-04 17:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_remove_user_name_remove_user_super_user_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="student",
            new_name="is_student",
        ),
        migrations.AlterField(
            model_name="user",
            name="is_superuser",
            field=models.BooleanField(default=False),
        ),
    ]
