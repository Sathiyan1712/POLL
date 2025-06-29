# Generated by Django 5.2.3 on 2025-06-26 08:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Poll",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("statement", models.CharField(max_length=255)),
                ("option1", models.CharField(max_length=55)),
                ("vote1", models.IntegerField(default=0)),
                ("option2", models.CharField(max_length=55)),
                ("vote2", models.IntegerField(default=0)),
                ("option3", models.CharField(max_length=55)),
                ("vote3", models.IntegerField(default=0)),
                ("delete_password", models.CharField(blank=True, max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name="Vote",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "poll",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.poll"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "unique_together": {("user", "poll")},
            },
        ),
    ]
