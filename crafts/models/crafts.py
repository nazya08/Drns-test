from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Craft(models.Model):
    craftsman = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="craftsman_crafts", verbose_name="Craftsman"
    )
    margin = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Margin"
    )
    price = models.PositiveIntegerField("Price")
    created_at = models.DateTimeField(
        verbose_name="Created at",
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="Updated at",
        auto_now=True
    )

    class Meta:
        verbose_name = 'Craft'
        verbose_name_plural = 'Crafts'
        ordering = ('-price',)

    def __str__(self):
        return f"Craft #{self.pk} by {self.craftsman}"
