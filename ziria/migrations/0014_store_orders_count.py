# Generated by Django 4.1.7 on 2023-05-12 02:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ziria", "0013_orderitem_item_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="store",
            name="orders_count",
            field=models.IntegerField(default=0),
        ),
    ]
