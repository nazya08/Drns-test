from django.contrib import admin

from shipment.models import Shipment, ShippingAddress, ShipmentInventory


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'receiver', 'shipping_full_name', 'shipping_phone_number', 'shipping_city', 'shipping_address',
    )
    list_display_links = ('id',)
    search_fields = ('receiver', 'shipping_city', 'shipping_second_name',)


@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'shipped_to', 'tracking_number', 'departure_date', 'arrival_date', 'status',)
    list_display_links = ('id',)
    empty_value_display = 'Unknown'
    list_filter = ('status',)
    radio_fields = {'status': admin.VERTICAL}


@admin.register(ShipmentInventory)
class ShipmentInventoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'shipment', 'inventory', 'quantity', 'created_at',)
    list_display_links = ('id',)
