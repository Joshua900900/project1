# Generated by Django 4.2.11 on 2024-05-02 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("simpleapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Fill_out",
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
                ("firstname", models.CharField(max_length=255)),
                ("lastname", models.CharField(max_length=255)),
                ("age", models.IntegerField()),
            ],
        ),
    ]