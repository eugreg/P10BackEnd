# Generated by Django 4.2.4 on 2023-09-05 11:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("uploader", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
                ("materialCommunityIcons", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Compra",
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
                    "status",
                    models.IntegerField(
                        choices=[
                            (1, "Carrinho"),
                            (2, "Realizado"),
                            (3, "Pago"),
                            (4, "Entregue"),
                        ],
                        default=1,
                    ),
                ),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="compras",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Descontos",
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
                (
                    "porcentagem",
                    models.DecimalField(decimal_places=2, max_digits=10, null=True),
                ),
            ],
            options={
                "verbose_name_plural": "Descontos",
            },
        ),
        migrations.CreateModel(
            name="Fornecedor",
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
                ("nome", models.CharField(max_length=100)),
                ("cnpj", models.CharField(max_length=100)),
                ("email", models.EmailField(default=None, max_length=254)),
                ("telefone", models.CharField(max_length=100)),
                ("endereco", models.CharField(max_length=100)),
                ("cep", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name_plural": "Fornecedores",
            },
        ),
        migrations.CreateModel(
            name="Marca",
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
                ("nome", models.CharField(max_length=100)),
                (
                    "imagem",
                    models.ManyToManyField(related_name="+", to="uploader.image"),
                ),
            ],
        ),
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
                ("descricao", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name_plural": "Sazonais",
            },
        ),
        migrations.CreateModel(
            name="SubCategoria",
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
                (
                    "categoria",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="subcategorias",
                        to="P10.categoria",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Produtos",
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
                ("nome", models.CharField(max_length=100)),
                ("descricao", models.CharField(max_length=150)),
                (
                    "preco",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                ("quantidade", models.IntegerField(default=0, null=True)),
                ("data", models.DateField()),
                ("tags", models.CharField(max_length=200)),
                (
                    "categoria",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="Produtos",
                        to="P10.categoria",
                    ),
                ),
                (
                    "desconto",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="Produtos",
                        to="P10.descontos",
                    ),
                ),
                (
                    "fornecedor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="Produtos",
                        to="P10.fornecedor",
                    ),
                ),
                (
                    "imagem",
                    models.ManyToManyField(related_name="+", to="uploader.image"),
                ),
                (
                    "marca",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="Produtos",
                        to="P10.marca",
                    ),
                ),
                (
                    "sazonal",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="Produtos",
                        to="P10.sazonal",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Produtos",
            },
        ),
        migrations.CreateModel(
            name="ItensCompra",
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
                ("quantidade", models.IntegerField(default=1)),
                ("preco_item", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "compra",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="itens",
                        to="P10.compra",
                    ),
                ),
                (
                    "produto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="P10.produtos",
                    ),
                ),
            ],
        ),
    ]
