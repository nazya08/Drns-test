from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


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
    first_name = models.CharField('First name', max_length=30)
    second_name = models.CharField('Second name', max_length=30)
    phone_number = models.CharField('Phone Number', max_length=20, unique=True)
    city = models.CharField('City', max_length=30)
    address = models.CharField('Address (Nova Post branch)', max_length=100, help_text='Nova Post branch')
    postal_code = models.CharField('Postal Code', max_length=20, blank=True, null=True)
    country = models.CharField('Country', max_length=30, default='Україна')

    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated at", auto_now=True)

    class Meta:
        verbose_name = "Shipping address"
        verbose_name_plural = "Shipping addresses"
        ordering = ('second_name',)
        unique_together = ('receiver', 'phone_number',)

    def __str__(self):
        return f"{self.full_name} - {self.address}, {self.city}"

    @property
    def full_name(self):
        return f'{self.second_name} {self.first_name}'


class Shipment(models.Model):
    # products = models.ManyToManyField('Inventory', related_name='shipments', verbose_name='Products')

    shipped_from_city = models.CharField(
        'Shipped from city', max_length=100, help_text='Enter the city of origin (Nova Post)'
    )
    shipped_from_branch = models.CharField(
        'Shipped from branch', max_length=100, help_text='Enter the branch of origin (Nova Post)'
    )
    shipped_to = models.ForeignKey(
        ShippingAddress, related_name='shipments', on_delete=models.CASCADE, verbose_name='Shipped to'
    )
    tracking_number = models.CharField('Tracking number', max_length=30, null=True, unique=True)
    departure_date = models.DateTimeField('Departure date', default=timezone.now)
    arrival_date = models.DateTimeField('Arrival date', blank=True, null=True)

    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated at", auto_now=True)

    class Meta:
        verbose_name = "Shipment"
        verbose_name_plural = "Shipments"

    def __str__(self):
        return f'Shipment #{self.pk} for {self.shipped_to.full_name}'


class ShipmentWarehouseItem(models.Model):
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE, related_name='shipment_warehouse_item')
    warehouse_item = models.ForeignKey(
        'inventory.WarehouseItems', on_delete=models.CASCADE, related_name='warehouse_item_shipment'
    )
    status = models.CharField(
        'Status', max_length=30, choices=ShippingStatus.choices, default=ShippingStatus.INDUCTED
    )

    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated at", auto_now=True)

    class Meta:
        verbose_name = 'Shipment WarehouseItems'
        verbose_name_plural = verbose_name
        ordering = ('created_at',)
        unique_together = ('shipment', 'warehouse_item',)

    def __str__(self):
        return f'{self.warehouse_item.item} in Shipment #{self.shipment.pk}'
