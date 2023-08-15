# Generated by Django 4.2.4 on 2023-08-15 12:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("P10", "0006_alter_descontos_options_alter_produtos_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="Sazonal",
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
                ("descrição", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name_plural": "Sazonal",
            },
        ),
    ]