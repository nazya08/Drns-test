from rest_framework import serializers

from orders.models.orders import Order


class OrderSerializer(serializers.ModelSerializer):
    # consumer = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

    # def get_consumer(self, obj):
    #     consumer_info = obj.consumer
    #     return {'id': consumer_info.id, 'username': consumer_info.username}
