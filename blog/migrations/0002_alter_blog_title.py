# Generated by Django 4.1.4 on 2023-01-02 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="title",
            field=models.CharField(max_length=250, unique=True, verbose_name="title"),
        ),
    ]
