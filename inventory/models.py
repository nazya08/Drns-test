import uuid

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from djmoney.models.fields import MoneyField

from drones.models import DronePart


class WarehouseItemsStatus(models.TextChoices):
    IN_STOCK = 'In Stock', _('In Stock')
    OUT_OF_STOCK = 'Out of Stock', _('Out of Stock')
    RESERVED = 'Reserved', _('Reserved')
    IN_TRANSIT = 'In Transit', _('In Transit')
    CONSUMED = 'Consumed', _('Consumed')
    RETURNED = 'Returned', _('Returned')
    DAMAGED = 'Damaged', _('Damaged')
    RECALLED = 'Recalled', _('Recalled')


class WarehouseItems(models.Model):
    # image = models.ImageField('Image', upload_to='inventory_images/', blank=True, null=True)
    # weight = models.FloatField('Weight', blank=True, null=True)

    article = models.UUIDField('Article', primary_key=True, default=uuid.uuid4, editable=False)
    item = models.ForeignKey(
        DronePart, on_delete=models.RESTRICT, related_name='warehouse_items', verbose_name='Item'
    )
    status = models.CharField(
        'Status', max_length=30, choices=WarehouseItemsStatus.choices, default=WarehouseItemsStatus.IN_STOCK
    )
    quantity = models.PositiveIntegerField('Quantity', default=0)
    safety_stock = models.PositiveIntegerField('Safety stock', default=0)
    # safety_stock може бути використане для попередження про нестачу товару
    purchase_price = MoneyField(
        "Purchase price", decimal_places=2, default_currency='UAH', max_digits=11, blank=True, null=True,
        help_text='Purchase price per 1 item'
    )

    supplier = models.ForeignKey(
        User, on_delete=models.RESTRICT, related_name='supplied_items', verbose_name='Supplier'
    )
    manager = models.ForeignKey(
        User, on_delete=models.RESTRICT, null=True, related_name='managed_warehouse_items', verbose_name='Manager'
    )

    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated at", auto_now=True)

    class Meta:
        verbose_name = "Warehouse Items"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'Warehouse item #{self.article} - {self.item.name}'
