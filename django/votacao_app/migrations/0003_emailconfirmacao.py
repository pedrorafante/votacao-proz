# Generated by Django 4.1.1 on 2023-06-25 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("votacao_app", "0002_validacao_emails"),
    ]

    operations = [
        migrations.CreateModel(
            name="EmailConfirmacao",
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
                ("emails", models.CharField(max_length=200)),
            ],
        ),
    ]
