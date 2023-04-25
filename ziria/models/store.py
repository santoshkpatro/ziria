from django.db import models

from .base import BaseModel


class Store(BaseModel):
    name = models.CharField(max_length=300)
    slug = models.SlugField(blank=True, unique=True)
    is_active = models.BooleanField(default=True)
    currency = models.CharField(max_length=3)
    country = models.CharField(max_length=3)
    payments_enabled = models.BooleanField(default=False)

    class Meta:
        db_table = "stores"

    def __str__(self) -> str:
        return self.name