# Generated by Django 4.1.5 on 2023-04-22 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp1", "0003_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AudioFile",
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
                ("audio_file", models.FileField(upload_to="audio/")),
            ],
        ),
    ]