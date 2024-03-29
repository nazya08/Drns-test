import uuid

from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Verification(models.Model):

    STATUS_CHOICES = (
        (1, "В очікуванні"),
        (2, "Підтверджено"),
        (3, "Відхилено"),
    )
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    status = models.IntegerField(
        choices=STATUS_CHOICES, default=1, verbose_name="Статус верифікації"
    )
    order = models.OneToOneField(
        'orders.Order', on_delete=models.CASCADE, verbose_name="Замовлення"
    )
    verified_by = models.ForeignKey(
        User, on_delete=models.RESTRICT, related_name="verification_orders", verbose_name="Користувач-верифікатор"
    )

    class Meta:
        verbose_name = "Верифікація"
        verbose_name_plural = "Верифікації"
        ordering = ('status',)

    def __str__(self):
        return f"Верифікація замовлення #{self.order} - {self.verified_by}"
