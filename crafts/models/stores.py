from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Store(models.Model):
    name = models.CharField("Назва", max_length=100)
    drone = models.ForeignKey(
        "drones.Drone", on_delete=models.CASCADE, related_name='stores', verbose_name='Дрон', blank=True
    )
    count = models.PositiveSmallIntegerField("Кількість")
    price_per_unit = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Ціна за одиницю в $"
    )
    craftsman = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Майстер"
    )

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазини'
        ordering = ('name',)
        unique_together = ['name', 'drone']

    def __str__(self):
        return f'{self.name} ({self.pk})'
