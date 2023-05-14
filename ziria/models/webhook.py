from django.db import models
from django.contrib.postgres.fields import ArrayField

from .base import BaseModel


class Webhook(BaseModel):
    class Source(models.TextChoices):
        PLUGIN = ("plugin", "Plugin")
        CUSTOM = ("custom", "Custom")

    class TargetContentType(models.TextChoices):
        JSON = ("json", "JSON")
        XML = ("xml", "XML")

    class Event(models.TextChoices):
        ORDER_CREATED = ("order.created", "Order Created")
        ORDER_UPDATED = ("order.updated", "Order Updated")

        PRODUCT_CREATED = ("product.created", "Product Created")
        PRODUCT_UPDATED = ("product.updated", "Product Updated")

    store = models.ForeignKey(
        "Store", on_delete=models.SET_NULL, related_name="webhooks", null=True
    )
    name = models.CharField(max_length=100)
    events = ArrayField(
        base_field=models.CharField(max_length=20, choices=Event.choices)
    )
    is_active = models.BooleanField(default=True)
    target_url = models.URLField()
    target_content_type = models.CharField(
        max_length=5, default=TargetContentType.JSON, choices=TargetContentType.choices
    )
    secret = models.CharField(max_length=50, blank=True, null=True)
    source = models.CharField(
        max_length=10, choices=Source.choices, default=Source.CUSTOM
    )

    class Meta:
        db_table = "webhooks"

    def __str__(self) -> str:
        return self.name
