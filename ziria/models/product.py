from django.db import models

from .base import BaseModel


class Product(BaseModel):
    class Status(models.TextChoices):
        ACTIVE = ("active", "ACTIVE")
        ARCHIVED = ("archived", "ARCHIVED")
        DRAFT = ("draft", "DRAFT")

    store = models.ForeignKey(
        "Store", on_delete=models.SET_NULL, related_name="store_products", null=True
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="category_products",
    )
    title = models.TextField()
    slug = models.SlugField(blank=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=10, default=Status.ACTIVE, choices=Status.choices
    )

    class Meta:
        db_table = "products"
        unique_together = ["store", "slug"]

    def __str__(self) -> str:
        return self.title
