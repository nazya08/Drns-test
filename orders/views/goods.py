from rest_framework import generics, filters
from rest_framework.permissions import IsAdminUser

from orders.models.goods import Goods, GoodDeal
from orders.permissions import IsAdminAllOrConsumerGet
from orders.serializers.goods import GoodsSerializer, GoodDealSerializer


class GoodsListCreate(generics.ListCreateAPIView):
    queryset = Goods.objects.select_related('order', 'drone')
    serializer_class = GoodsSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['created_at', 'count']
    search_fields = ['type', 'drone__name']
    permission_classes = (IsAdminUser,)


class GoodsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    permission_classes = (IsAdminUser,)


class GoodDealListCreate(generics.ListCreateAPIView):
    queryset = GoodDeal.objects.select_related('goods')
    serializer_class = GoodDealSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['created_at', 'count']
    search_fields = ['goods__drone__name']
    permission_classes = (IsAdminUser,)


class GoodDealRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = GoodDeal.objects.all()
    serializer_class = GoodDealSerializer
    permission_classes = (IsAdminAllOrConsumerGet,)

