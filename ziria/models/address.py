from django.db import models

from ziria.models.base import BaseModel


class Address(BaseModel):
    class AddressType(models.TextChoices):
        BILLING = ("billing", "Billing")
        SHIPPING = ("shipping", "Shipping")
        PICK_UP = ("pick_up", "Pick Up")

    store = models.ForeignKey(
        "Store", on_delete=models.SET_NULL, null=True, related_name="store_addresses"
    )
    customer = models.ForeignKey(
        "Customer",
        on_delete=models.SET_NULL,
        related_name="customer_addresses",
        null=True,
    )
    address_type = models.CharField(max_length=10, choices=AddressType.choices)
    full_name = models.CharField(max_length=300)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    country_code = models.CharField(max_length=3)
    state = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=100)
    zip = models.CharField(max_length=10, blank=True, null=True)
    address1 = models.TextField(blank=True, null=True)
    address2 = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "addresses"

    def __str__(self) -> str:
        return str(self.id)
