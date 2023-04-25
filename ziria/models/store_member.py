from django.db import models
from django.contrib.postgres.fields import ArrayField

from .base import BaseModel


class StoreMember(BaseModel):
    class Role(models.TextChoices):
        ADMIN = ("admin", "ADMIN")
        OWNER = ("owner", "OWNER")
        STAFF = ("staff", "STAFF")

    class Permission(models.TextChoices):
        ORDER_CREATE = ("order.create", "Order Create")
        ORDER_VIEW = ("order.view", "Order View")
        ORDER_EDIT = ("order.edit", "Order Edit")
        ORDER_DELETE = ("order.delete", "Order Delete")

        CUSTOMER_CREATE = ("customer.create", "Customer Create")
        CUSTOMER_VIEW = ("customer.view", "Customer View")
        CUSTOMER_EDIT = ("customer.edit", "Customer Edit")
        CUSTOMER_DELETE = ("customer.delete", "Customer Delete")

    store = models.ForeignKey(
        "Store", on_delete=models.CASCADE, related_name="store_members"
    )
    user = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="user_members"
    )
    is_active = models.BooleanField(default=True)
    role = models.CharField(max_length=5, default=Role.ADMIN, choices=Role.choices)
    staff_permissions = ArrayField(
        base_field=models.CharField(max_length=20, choices=Permission.choices),
        blank=True,
        null=True,
    )

    class Meta:
        db_table = "store_members"
        unique_together = ["store", "user"]

    def __str__(self) -> str:
        return str(self.id)
