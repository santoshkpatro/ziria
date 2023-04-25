from django.db import models

from .base import BaseModel


class ProductVariant(BaseModel):
    class Status(models.TextChoices):
        ACTIVE = ("active", "ACTIVE")
        ARCHIVED = ("archived", "ARCHIVED")
        DRAFT = ("draft", "DRAFT")

    class Unit(models.TextChoices):
        PIECE = ("piece", "PIECE")
        KG = ("kg", "KG")
        GM = ("gm", "GM")
        LITRE = ("litre", "LITRE")
        ML = ("ml", "ML")
        BUNDLE = ("bundle", "BUNDLE")

    store = models.ForeignKey(
        "Store",
        on_delete=models.SET_NULL,
        related_name="store_product_variants",
        null=True,
    )
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, related_name="product_variants"
    )
    title = models.TextField()
    is_base_variant = models.BooleanField(default=True)
    position = models.IntegerField(blank=True, default=1)
    is_active = models.BooleanField(default=True)
    unit = models.CharField(max_length=10, choices=Unit.choices, default=Unit.PIECE)
    old_price = models.IntegerField(blank=True)
    price = models.IntegerField()
    currency = models.CharField(max_length=3)
    sku = models.CharField(max_length=20, blank=True, null=True)
    has_inventory = models.BooleanField(default=False)
    status = models.CharField(
        max_length=10, default=Status.ACTIVE, choices=Status.choices
    )

    class Meta:
        db_table = "product_variants"

    def __str__(self) -> str:
        return str(self.id)
