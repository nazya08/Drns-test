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
        choices=STATUS_CHOICES, default=1, verbose_name="Status of verification"
    )
    order = models.OneToOneField(
        'orders.Order', on_delete=models.CASCADE, verbose_name="Order"
    )
    verified_by = models.ForeignKey(
        User, on_delete=models.RESTRICT, related_name="verification_orders", verbose_name="Verifier"
    )

    class Meta:
        verbose_name = "Verification"
        verbose_name_plural = "Verifications"
        ordering = ('status',)

    def __str__(self):
        return f"Verification #{self.order} - {self.verified_by}"
