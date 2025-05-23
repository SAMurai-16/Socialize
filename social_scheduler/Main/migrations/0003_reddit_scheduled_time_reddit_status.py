# Generated by Django 5.2 on 2025-05-12 06:19

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Main", "0002_reddit"),
    ]

    operations = [
        migrations.AddField(
            model_name="reddit",
            name="scheduled_time",
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="reddit",
            name="status",
            field=models.CharField(default="Pending", max_length=10),
        ),
    ]
