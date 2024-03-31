from django.contrib import admin

from common.models import mixins
from crafts.models import stores, crafts


@admin.register(stores.Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'show_drones')
    list_filter = ('name',)

    def show_drones(self, obj):
        drone = obj.drone
        if drone:
            return f"{drone.name} ({obj.count} шт.) - {obj.price_per_unit}$ - {obj.craftsman}"

    show_drones.short_description = "Drones"


@admin.register(crafts.Craft)
class CraftAdmin(admin.ModelAdmin):
    list_display = ('id', 'craftsman_link', 'margin', 'price', 'created_at', 'updated_at')
    list_display_links = ('id',)

    def craftsman_link(self, obj):
        return mixins.LinkMixin.link_to_object(obj.craftsman, 'auth_user')
