from django.contrib.auth.models import User
from django.db import models

from inventory.models import Inventory

INVENTORY_STATUS_CODES = (
    ('0', 'Inducted'),
    ('1', 'Order received'),
    ('2', 'Order started'),
    ('3', 'Order completed'),
    ('4', 'Shipped'),
)


class Shipment(models.Model):
    owner = models.ForeignKey(User, related_name='shipments', on_delete=models.CASCADE)
    palletized = models.BooleanField(default=False)
    arrival = models.DateField()
    departure = models.DateField(null=True)
    labor_time = models.IntegerField()
    notes = models.TextField(null=True)
    tracking_number = models.CharField(max_length=30, null=True)
    status = models.CharField(max_length=30, choices=INVENTORY_STATUS_CODES, default=0)

    def __str__(self):
        return f'Shipment #{self.pk}: {self.arrival}'


class ShipmentInventory(models.Model):
    shipment = models.ForeignKey(Shipment, related_name='shipment_inventory', on_delete=models.CASCADE)
    inventory = models.ForeignKey(Inventory, related_name='shipment_inventory', on_delete=models.CASCADE)
    arrival_date = models.DateField()
    quantity_in_shipment = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.inventory} in Shipment #{self.shipment.pk}'
