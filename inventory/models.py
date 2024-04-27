import uuid

from django.contrib.auth.models import User
from django.db import models
from djmoney.models.fields import MoneyField

from drones.models import DronePart


class Inventory(models.Model):
    article = models.UUIDField('Article', primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(
        DronePart, on_delete=models.RESTRICT, null=True, related_name='inventory_items', verbose_name='Product'
    )
    image = models.ImageField('Image', upload_to='inventory_images/', blank=True, null=True)
    weight = models.FloatField('Weight', blank=True, null=True)
    status = models.CharField('Status', max_length=30)
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
        User, on_delete=models.RESTRICT, null=True, related_name='inventory', verbose_name='Manager'
    )

    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated at", auto_now=True)

    def __str__(self):
        return f'Inventory item #{self.article} - {self.product.name}'
