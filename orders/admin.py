from django.contrib import admin

from orders.models import orders, verification, goods
from common.models import mixins


@admin.register(orders.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'consumer_link', 'created_at', 'updated_at',)
    list_display_links = ('id',)
    list_filter = ('consumer',)
    search_fields = ('id',)

    def consumer_link(self, obj):
        return mixins.LinkMixin.link_to_object(obj.consumer, 'auth_user')


@admin.register(verification.Verification)
class VerificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_link', 'verifier_link', 'status',)
    list_display_links = ('id',)
    list_filter = ('status', 'verified_by')
    search_fields = ('id',)
    radio_fields = {'status': admin.VERTICAL}

    def order_link(self, obj):
        return mixins.LinkMixin.link_to_object(obj.order, 'orders_order')

    def verifier_link(self, obj):
        return mixins.LinkMixin.link_to_object(obj.verified_by, 'auth_user')


@admin.register(goods.Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_link', 'drone_link', 'count', 'type',)
    list_display_links = ('id',)
    search_fields = ('type',)

    def order_link(self, obj):
        return mixins.LinkMixin.link_to_object(obj.order, 'orders_order')

    def drone_link(self, obj):
        return mixins.LinkMixin.link_to_object(obj.drone, 'drones_drone')


@admin.register(goods.GoodDeal)
class GoodDealAdmin(admin.ModelAdmin):
    list_display = ('id', 'store', 'craft', 'goods', 'status', 'count', 'payment', 'type')
    list_filter = ('status', 'payment', 'type')
    search_fields = ('store__name', 'craft__id', 'goods__id')
    readonly_fields = ('id',)
