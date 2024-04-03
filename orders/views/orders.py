from rest_framework import generics, filters
from rest_framework.permissions import IsAdminUser

from orders.permissions import IsAdminOrConsumer
from orders.models.orders import Order
from orders.serializers.orders import OrderSerializer


class OrderListCreate(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    ordering_fields = ['created_at']
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['consumer__id', 'consumer__username']

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminOrConsumer()]
        return [IsAdminUser()]


class OrderRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_permissions(self):
        if self.request.method in ['GET', 'DELETE']:
            return [IsAdminOrConsumer()]
        return [IsAdminUser()]