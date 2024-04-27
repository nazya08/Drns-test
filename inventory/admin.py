from django.contrib import admin
from .models import Inventory


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = (
        'article', 'part_of_drone', 'quantity', 'safety_stock', 'purchase_price', 'supplier', 'manager', 'status'
    )
    list_display_links = ('article',)
    list_filter = ('status', 'supplier', 'product',)

    def part_of_drone(self, obj):
        return obj.product.name
