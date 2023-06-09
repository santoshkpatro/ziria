# Generated by Django 4.1.7 on 2023-05-12 18:06

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("ziria", "0016_alter_order_order_status"),
    ]

    operations = [
        migrations.CreateModel(
            name="Plugin",
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
                ("name", models.CharField(max_length=100)),
                ("status", models.CharField(max_length=20)),
                ("key", models.CharField(blank=True, max_length=100)),
                ("secret", models.CharField(blank=True, max_length=100)),
                (
                    "store",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="plugins",
                        to="ziria.store",
                    ),
                ),
            ],
            options={
                "db_table": "plugins",
                "unique_together": {("store", "name")},
            },
        ),
    ]
