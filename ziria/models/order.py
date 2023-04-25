from django.db import models
from django.contrib.postgres.fields import ArrayField

from .base import BaseModel


class Order(BaseModel):
    class OrderStatus(models.TextChoices):
        OPEN = ("open", "Open")
        ARCHIVED = ("archived", "Archived")
        CANCELLED = ("cancelled", "Cancelled")

    class PaymentStatus(models.TextChoices):
        PENDING = ("pending", "Pending")
        AUTHORIZED = ("authorized", "Authorized")
        PAID = ("paid", "Paid")
        UNPAID = ("unpaid", "Unpaid")
        PARTIAL_PAID = ("partial_paid", "Partial Paid")
        REFUNDED = ("refunded", "Refunded")
        PARTIAL_REFUNDED = ("partial_refunded", "Partial Refunded")
        UNKNOWN = ("unknown", "Unknown")

    class FulfillmentStatus(models.TextChoices):
        FULFILLED = ("fulfilled", "Fulfilled")
        UNFULFILLED = ("unfulfilled", "Unfulfilled")
        PARTIALLY_FULFILLED = ("partially_fulfilled", "Partially Fulfilled")
        SCHEDULED = ("scheduled", "Scheduled")
        ON_HOLD = ("on_hold", "On Hold")

    class ReturnStatus(models.TextChoices):
        REQUESTED = ("requested", "Requested")
        IN_PROGRESS = ("in_progress", "In Progress")
        RETURNED = ("returned", "Returned")
        INSPECTION = ("inspection", "Inspection")
        FAILED = ("failed", "Failed")

    class PaymentMethod(models.TextChoices):
        ONLINE = ("online", "Online")
        COD = ("cod", "Cash On Delivery")

    store = models.ForeignKey(
        "Store", on_delete=models.SET_NULL, null=True, related_name="store_orders"
    )
    customer = models.OneToOneField(
        "Customer", on_delete=models.SET_NULL, null=True, blank=True, related_name="customer_ordders"
    )
    order_number = models.IntegerField(blank=True, null=True)
    order_id = models.CharField(max_length=10, blank=True, editable=False)
    currency = models.CharField(max_length=3)
    order_status = models.CharField(
        max_length=10, default=OrderStatus.OPEN, choices=OrderStatus.choices
    )
    payment_status = models.CharField(
        max_length=20, default=PaymentStatus.UNKNOWN, choices=PaymentStatus.choices
    )
    payment_provider = models.CharField(max_length=10, blank=True, null=True)
    payment_method = models.CharField(max_length=10, choices=PaymentMethod.choices)
    fulfillment_status = models.CharField(
        max_length=20,
        default=FulfillmentStatus.UNFULFILLED,
        choices=FulfillmentStatus.choices,
    )
    return_status = models.CharField(
        max_length=20, choices=ReturnStatus.choices, blank=True, null=True
    )
    payment_id = models.TextField(blank=True, null=True)
    transaction_id = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    is_order_placed = models.BooleanField(default=False)
    placed_at = models.DateTimeField(blank=True, null=True)
    is_test_order = models.BooleanField(default=False)
    tags = ArrayField(base_field=models.CharField(max_length=20), blank=True, null=True)
    shipping_address = models.OneToOneField(
        "Address",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="shipping_orders",
    )
    billing_address = models.OneToOneField(
        "Address",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="billing_orders",
    )

    class Meta:
        db_table = "orders"
        unique_together = ["store", "order_number"]

    def __str__(self) -> str:
        return str(self.id)
