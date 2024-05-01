from django.contrib import admin

from shipment.models import Shipment, ShippingAddress, ShipmentWarehouseItem


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'receiver', 'full_name', 'phone_number', 'city', 'address', 'country',
    )
    list_display_links = ('id',)
    search_fields = ('receiver', 'city', 'second_name',)


@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'shipped_to',
        'shipped_from_city',
        'shipped_from_branch',
        'tracking_number',
        'departure_date',
        'arrival_date',
        'created_at',
        'updated_at',
    )
    list_display_links = ('id',)
    empty_value_display = 'Unknown'


@admin.register(ShipmentWarehouseItem)
class ShipmentInventoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'shipment', 'warehouse_item', 'status', 'created_at',)
    list_display_links = ('id',)
    list_filter = ('status',)
    radio_fields = {'status': admin.VERTICAL}
