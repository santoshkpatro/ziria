from django.db import models

from .base import BaseModel


class Discount(BaseModel):
    class Status(models.TextChoices):
        ACTIVE = ("active", "ACTIVE")
        ARCHIVED = ("archived", "ARCHIVED")
        DRAFT = ("draft", "DRAFT")

    class DiscountType(models.TextChoices):
        AMOUNT = ("amount", "Amount")
        PERCENTAGE = ("percentage", "Percentage")

    class DiscountAllocation(models.TextChoices):
        ENTIRE_ORDER = ("entire_order", "Entire Order")
        SPECIFIC_PRODUCT = ("specific_product", "Specific Product")

    store = models.ForeignKey(
        "Store", on_delete=models.SET_NULL, null=True, related_name="store_discounts"
    )
    description = models.TextField(blank=True, null=True)
    code = models.CharField(max_length=100, blank=True, null=True)
    discount_type = models.CharField(
        max_length=12, choices=DiscountType.choices
    )
    discount_value = models.IntegerField()
    discount_allocation = models.CharField(
        max_length=20, choices=DiscountAllocation.choices
    )
    max_discount = models.IntegerField(blank=True, null=True)
    min_order_value = models.IntegerField(blank=True, null=True)
    uses_per_customer = models.IntegerField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    currency = models.CharField(max_length=3)
    status = models.CharField(
        max_length=10, default=Status.DRAFT, choices=Status.choices
    )
    allow_multiple_discounts = models.BooleanField(default=False)

    class Meta:
        db_table = "discounts"

    def __str__(self) -> str:
        return self.code
