# Generated by Django 4.2.14 on 2024-07-26 04:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("inventory", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="food_product",
            field=models.BooleanField(default=False),
        ),
    ]