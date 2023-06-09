# Generated by Django 4.1.7 on 2023-04-25 17:31

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("ziria", "0009_order"),
    ]

    operations = [
        migrations.CreateModel(
            name="OrderItem",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("currency", models.CharField(max_length=3)),
                ("quantity", models.IntegerField(default=1)),
                ("price", models.IntegerField()),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="order_items",
                        to="ziria.order",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="product_order_items",
                        to="ziria.product",
                    ),
                ),
                (
                    "product_variant",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="product_variant_order_items",
                        to="ziria.productvariant",
                    ),
                ),
                (
                    "store",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="store_order_items",
                        to="ziria.store",
                    ),
                ),
            ],
            options={
                "db_table": "order_items",
            },
        ),
    ]
