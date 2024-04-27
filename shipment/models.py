from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from inventory.models import Inventory


class ShippingStatus(models.TextChoices):
    INDUCTED = 'Inducted', _('Inducted')
    ORDER_RECEIVED = 'Order received', _('Order received')
    ORDER_STARTED = 'Order started', _('Order started')
    ORDER_COMPLETED = 'Order completed', _('Order completed')
    SHIPPED = 'Shipped', _('Shipped')


class ShippingAddress(models.Model):
    receiver = models.ForeignKey(
        User, related_name='shipping_address', on_delete=models.CASCADE, verbose_name='Craftsman-receiver'
    )
    shipping_first_name = models.CharField('First name', max_length=30)
    shipping_second_name = models.CharField('Second name', max_length=30)
    shipping_phone_number = models.CharField('Phone Number', max_length=20, unique=True)
    shipping_city = models.CharField('City', max_length=30)
    shipping_address = models.CharField('Shipping Address', max_length=100, help_text='Nova Post branch')
    shipping_postal_code = models.CharField('Postal Code', max_length=20, blank=True, null=True)
    shipping_country = models.CharField('Country', max_length=30, default='Україна')

    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated at", auto_now=True)

    class Meta:
        verbose_name = "Shipping address"
        verbose_name_plural = "Shipping addresses"
        ordering = ('shipping_second_name',)
        unique_together = ('receiver', 'shipping_phone_number',)

    def __str__(self):
        return f"{self.shipping_full_name} - {self.shipping_address}"

    @property
    def shipping_full_name(self):
        return f'{self.shipping_second_name} {self.shipping_first_name}'


class Shipment(models.Model):
    shipped_to = models.ForeignKey(ShippingAddress, related_name='shipments', on_delete=models.CASCADE)
    # products = models.ManyToManyField('Inventory', related_name='shipments', verbose_name='Products')
    tracking_number = models.CharField('Tracking number', max_length=30, null=True, unique=True)
    departure_date = models.DateTimeField('Departure date', default=timezone.now)
    arrival_date = models.DateTimeField('Arrival date', blank=True, null=True)
    status = models.CharField(max_length=30, choices=ShippingStatus.choices, default=ShippingStatus.INDUCTED)

    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated at", auto_now=True)

    class Meta:
        verbose_name = "Shipment"
        verbose_name_plural = "Shipments"

    def __str__(self):
        return f'Shipment #{self.pk} for {self.shipped_to.shipping_full_name}'


class ShipmentInventory(models.Model):
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE, related_name='shipment_inventory')
    inventory = models.ForeignKey('inventory.Inventory', on_delete=models.CASCADE, related_name='shipment_inventory')
    quantity = models.PositiveIntegerField('Quantity')

    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated at", auto_now=True)

    class Meta:
        verbose_name = 'Shipment Inventory'
        verbose_name_plural = 'Shipment Inventories'
        ordering = ('created_at',)
        unique_together = ('shipment', 'inventory',)

    def __str__(self):
        return f'{self.inventory.product} - {self.quantity} units in Shipment #{self.shipment.pk}'

