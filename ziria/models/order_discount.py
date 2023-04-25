from django.db import models

from .base import BaseModel


class OrderDiscount(BaseModel):
    class DiscountType(models.TextChoices):
        AMOUNT = ("amount", "Amount")
        PERCENTAGE = ("percentage", "Percentage")

    class DiscountAllocation(models.TextChoices):
        ENTIRE_ORDER = ("entire_order", "Entire Order")
        SPECIFIC_PRODUCT = ("specific_product", "Specific Product")

    store = models.ForeignKey(
        "Store",
        on_delete=models.SET_NULL,
        null=True,
        related_name="store_order_discounts",
    )
    discount = models.ForeignKey(
        "Discount",
        on_delete=models.SET_NULL,
        null=True,
        related_name="discount_order_discounts",
    )
    discount_type = models.CharField(max_length=12, choices=DiscountType.choices)
    discount_value = models.IntegerField()
    discount_allocation = models.CharField(
        max_length=20, choices=DiscountAllocation.choices
    )
    order_item = models.ForeignKey(
        "OrderItem",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="order_item_order_discounts",
    )

    class Meta:
        db_table = "order_discounts"

    def __str__(self) -> str:
        return str(self.id)
