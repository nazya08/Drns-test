from django.contrib import admin

from shipment.models import Shipment, ShipmentInventory

admin.site.register(Shipment)
admin.site.register(ShipmentInventory)
