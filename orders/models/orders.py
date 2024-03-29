import uuid

from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Order(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    consumer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="orders", verbose_name="Замовник"
    )
    created_at = models.DateTimeField(
        verbose_name="Створено",
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="Змінено",
        auto_now=True
    )

    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = verbose_name
        ordering = ('created_at',)

    def __str__(self):
        return f"Замовлення #{self.pk} від {self.consumer}"
