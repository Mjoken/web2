# Generated by Django 4.2.7 on 2023-12-14 19:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="StudySession",
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
                ("group", models.CharField(max_length=10)),
                ("title", models.CharField(max_length=255)),
                (
                    "short_title",
                    models.CharField(
                        blank=True, default="Мат.Анализ", max_length=10, null=True
                    ),
                ),
                (
                    "session_type",
                    models.PositiveSmallIntegerField(blank=True, default=0, null=True),
                ),
                (
                    "subgroup",
                    models.PositiveSmallIntegerField(blank=True, default=0, null=True),
                ),
                (
                    "comment",
                    models.TextField(
                        blank=True, default="Здесь могла быть ваша заметка", null=True
                    ),
                ),
                ("date_start", models.DateField(auto_now_add=True)),
                ("time_start", models.TimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="email address"
                    ),
                ),
                ("first_name", models.CharField(max_length=55)),
                ("last_name", models.CharField(max_length=55)),
                ("second_name", models.CharField(max_length=55)),
                ("group", models.CharField(max_length=10)),
                (
                    "subgroup",
                    models.PositiveSmallIntegerField(blank=True, default=1, null=True),
                ),
                ("is_staff", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "id_card",
                    models.SmallIntegerField(
                        unique=True,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(9999999),
                        ],
                    ),
                ),
                ("is_mag", models.BooleanField(default=False)),
                ("is_student", models.BooleanField(default=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "db_table": "auth_user",
            },
        ),
    ]
