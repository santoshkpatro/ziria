from django.db import models

from .base import BaseModel


class OrderItem(BaseModel):
    class ItemType(models.TextChoices):
        PURCHASE = ("purchase", "Purchase")
        REFUND = ("refund", "refund")
        RETURN = ("return", "return")

    store = models.ForeignKey(
        "Store", on_delete=models.SET_NULL, null=True, related_name="store_order_items"
    )
    order = models.ForeignKey(
        "Order", on_delete=models.CASCADE, related_name="order_items"
    )
    item_type = models.CharField(
        max_length=10, choices=ItemType.choices, default=ItemType.PURCHASE
    )
    product = models.ForeignKey(
        "Product",
        on_delete=models.SET_NULL,
        related_name="product_order_items",
        null=True,
    )
    product_variant = models.ForeignKey(
        "ProductVariant",
        on_delete=models.SET_NULL,
        null=True,
        related_name="product_variant_order_items",
    )
    currency = models.CharField(max_length=3)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()

    class Meta:
        db_table = "order_items"

    def __str__(self) -> str:
        return str(self.id)
