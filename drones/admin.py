from django.contrib import admin

from .models import Drone, DronePart, DroneDronePart


@admin.register(Drone)
class DroneAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'priority', 'status')
    list_display_links = ('id',)
    list_filter = ('priority', 'status',)
    search_fields = ('name',)


@admin.register(DronePart)
class DronePartAdmin(admin.ModelAdmin):
    pass


@admin.register(DroneDronePart)
class DroneDronePartAdmin(admin.ModelAdmin):
    pass
