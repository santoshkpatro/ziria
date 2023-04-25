from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .base import BaseModel


class Customer(BaseModel, AbstractBaseUser):
    store = models.ForeignKey(
        "Store", on_delete=models.SET_NULL, null=True, related_name="store_customers"
    )
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    full_name = models.CharField(max_length=200)
    is_guest_user = models.BooleanField(default=False)

    USERNAME_FIELD = "id"

    class Meta:
        db_table = "customers"

    def __str__(self) -> str:
        if self.email:
            return self.email
        elif self.phone:
            return self.phone
        else:
            return self.full_name
