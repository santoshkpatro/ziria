from django.db import models

from .base import BaseModel


class Category(BaseModel):
    store = models.ForeignKey(
        "Store", on_delete=models.CASCADE, related_name="categories"
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="parent_categories",
    )
    name = models.CharField(max_length=200)
    slug = models.SlugField(blank=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        db_table = "categories"
        unique_together = ["store", "slug"]

    def __str__(self) -> str:
        return self.name
