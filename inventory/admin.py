from django.contrib import admin

from common.models import mixins
from .models import WarehouseItems


@admin.register(WarehouseItems)
class InventoryAdmin(admin.ModelAdmin):
    list_display = (
        'article', 'part_of_drone', 'quantity', 'safety_stock', 'purchase_price', 'supplier', 'manager', 'status'
    )
    list_display_links = ('article',)
    list_filter = ('status', 'supplier', 'item',)

    def part_of_drone(self, obj):
        return obj.item.name

    # def part_of_drone_link(self, obj):
    #     return mixins.LinkMixin.link_to_object(obj.store, 'crafts_store')
