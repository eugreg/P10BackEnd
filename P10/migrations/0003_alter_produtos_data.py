# Generated by Django 4.2.4 on 2023-08-31 18:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("P10", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="produtos",
            name="data",
            field=models.DateField(),
        ),
    ]
