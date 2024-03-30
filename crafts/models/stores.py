from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Store(models.Model):
    name = models.CharField("Name", max_length=100)
    drone = models.ForeignKey(
        "drones.Drone", on_delete=models.CASCADE, related_name='stores', verbose_name='Drone', blank=True
    )
    count = models.PositiveSmallIntegerField("Count")
    price_per_unit = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Price per unit in $"
    )
    craftsman = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="craftsman_stores", verbose_name="Craftsman"
    )

    class Meta:
        verbose_name = 'Store'
        verbose_name_plural = 'Stores'
        ordering = ('name',)
        unique_together = ['name', 'drone']

    def __str__(self):
        return f'{self.name} ({self.pk})'
