# Generated by Django 5.2 on 2025-05-14 19:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Main", "0010_remove_reddit_password_remove_reddit_username"),
    ]

    operations = [
        migrations.AddField(
            model_name="redditaccount",
            name="username",
            field=models.TextField(default="default_user"),
        ),
    ]
