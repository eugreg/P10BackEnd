# Generated by Django 4.2.4 on 2023-08-22 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("P10", "0008_alter_sazonal_options_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="produtos",
            name="subcategoria",
        ),
        migrations.AddField(
            model_name="produtos",
            name="sazonal",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="Produtos",
                to="P10.sazonal",
            ),
        ),
    ]