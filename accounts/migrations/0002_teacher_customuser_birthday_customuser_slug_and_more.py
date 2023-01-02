# Generated by Django 4.1.4 on 2023-01-01 00:10

import datetime
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Teacher",
            fields=[
                (
                    "customuser_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("reviwed", models.IntegerField(verbose_name="reviewed")),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            bases=("accounts.customuser",),
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name="customuser",
            name="birthday",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 1, 1, 0, 10, 12, 771630),
                verbose_name="birthday",
            ),
        ),
        migrations.AddField(
            model_name="customuser",
            name="slug",
            field=models.SlugField(default="5/10/1999", verbose_name="slug"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="customuser",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="updated_at"),
        ),
        migrations.CreateModel(
            name="Review",
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
                    "rate",
                    models.CharField(
                        choices=[
                            ("1", "1"),
                            ("2", "2"),
                            ("3", "3"),
                            ("4", "4"),
                            ("5", "5"),
                        ],
                        max_length=50,
                        verbose_name="rate",
                    ),
                ),
                (
                    "teacher",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.teacher",
                        verbose_name="teacher",
                    ),
                ),
            ],
        ),
    ]
