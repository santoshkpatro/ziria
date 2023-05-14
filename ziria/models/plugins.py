from django.db import models

from .base import BaseModel


class Plugin(BaseModel):
    class Status(models.TextChoices):
        TESTING = ("testing", "Testing")
        REVIEWING = ("reviewing", "Reviewing")
        LIVE = ("live", "Live")
        REJECTED = ("rejected", "Rejected")

    store = models.ForeignKey("Store", on_delete=models.SET_NULL, null=True, related_name="plugins")
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    key = models.CharField(max_length=100, blank=True)
    secret = models.CharField(max_length=100, blank=True)

    class Meta:
        unique_together = ["store", "name"]
        db_table = "plugins"

    def __str__(self) -> str:
        return self.name