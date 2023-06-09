# Generated by Django 4.1.7 on 2023-04-25 16:07

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("ziria", "0002_store"),
    ]

    operations = [
        migrations.CreateModel(
            name="StoreMember",
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
                ("is_active", models.BooleanField(default=True)),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("admin", "ADMIN"),
                            ("owner", "OWNER"),
                            ("staff", "STAFF"),
                        ],
                        default="admin",
                        max_length=5,
                    ),
                ),
                (
                    "staff_permissions",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(
                            choices=[
                                ("order.create", "Order Create"),
                                ("order.view", "Order View"),
                                ("order.edit", "Order Edit"),
                                ("order.delete", "Order Delete"),
                                ("customer.create", "Customer Create"),
                                ("customer.view", "Customer View"),
                                ("customer.edit", "Customer Edit"),
                                ("customer.delete", "Customer Delete"),
                            ],
                            max_length=20,
                        ),
                        blank=True,
                        null=True,
                        size=None,
                    ),
                ),
                (
                    "store",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="store_members",
                        to="ziria.store",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_members",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "store_members",
                "unique_together": {("store", "user")},
            },
        ),
    ]
