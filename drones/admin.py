from django.contrib import admin

from .models import Drone


@admin.register(Drone)
class DroneAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'priority', 'status')
    list_display_links = ('id',)
    list_filter = ('priority', 'status',)
    search_fields = ('name',)
