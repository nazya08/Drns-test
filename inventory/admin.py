from django.contrib import admin
from .models import Inventory


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('article', 'part_of_drone', 'manager', 'supplier', 'quantity', 'status')
    list_display_links = ('article',)

    def part_of_drone(self, obj):
        return obj.product.name
