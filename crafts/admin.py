from django.contrib import admin

from crafts.models import stores


@admin.register(stores.Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'show_drones')

    def show_drones(self, obj):
        drone = obj.drone
        if drone:
            return f"{drone.name} ({obj.count} шт.) - {obj.price_per_unit}$ - {obj.craftsman}"
        else:
            return "Дрон відсутній"
    show_drones.short_description = "Дрони"
