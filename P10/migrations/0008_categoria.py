# Generated by Django 4.2.2 on 2023-08-01 18:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("P10", "0007_alter_fornecedor_cnpj"),
    ]

    operations = [
        migrations.CreateModel(
            name="Categoria",
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
                ("descricao", models.CharField(max_length=100)),
            ],
        ),
    ]
