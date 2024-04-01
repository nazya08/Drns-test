import uuid
from enum import Enum

from django.db import models


class GoodDealStatus(Enum):
    WAIT = "В очікуванні"
    CONFIRMED = "Підтверджено"
    UNCONFIRMED = "Непідтверджено"


class PaymentIntent(Enum):
    BUY_READY_DRONE = "Оплата за готовий дрон"
    ORDER_DRONE_ASSEMBLY = "Замовлення на збірку дрона"


class GoodDealType(Enum):
    BUY_READY = "Купити готовий товар"
    ORDER = "Замовити товар"


class Goods(models.Model):
    order = models.ForeignKey(
        "orders.Order", on_delete=models.RESTRICT, related_name="goods", verbose_name="Order"
    )
    drone = models.ForeignKey(
        "drones.Drone", on_delete=models.CASCADE, related_name="goods", verbose_name="Drone"
    )
    count = models.PositiveSmallIntegerField("Count")
    type = models.CharField(
        "Type", max_length=35
    )
    created_at = models.DateTimeField(
        verbose_name="Created at",
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="Updated at",
        auto_now=True
    )

    class Meta:
        verbose_name = 'Goods'
        verbose_name_plural = verbose_name
        ordering = ('created_at',)
        unique_together = ['order', 'drone']

    def __str__(self):
        return f"Goods #{self.pk}"


class GoodDeal(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    store = models.ForeignKey(
        "crafts.Store", on_delete=models.PROTECT, related_name="goods_deals", verbose_name="Store"
    )
    craft = models.ForeignKey(
        "crafts.Craft", on_delete=models.PROTECT, related_name="goods_deals", verbose_name="Craft"
    )
    goods = models.ForeignKey(
        Goods, on_delete=models.PROTECT, related_name="goods_deals", verbose_name="Goods"
    )
    status = models.CharField(
        "Status", max_length=20,
        choices=[(tag.name, tag.value) for tag in GoodDealStatus], default=GoodDealStatus.WAIT.value
    )
    count = models.PositiveSmallIntegerField("Count")
    payment = models.CharField(
        "Payment", max_length=30,
        choices=[(tag.name, tag.value) for tag in PaymentIntent],
    )
    type = models.CharField(
        "Type", max_length=30,
        choices=[(tag.name, tag.value) for tag in GoodDealType],
    )
    created_at = models.DateTimeField(
        verbose_name="Created at",
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="Updated at",
        auto_now=True
    )

    class Meta:
        verbose_name = 'Good Deal'
        verbose_name_plural = 'Good Deals'
        ordering = ('created_at', 'status')

    def __str__(self):
        return f"Good-Deal #{self.pk}"
