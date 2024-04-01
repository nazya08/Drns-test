from rest_framework import generics, filters
from rest_framework.permissions import IsAdminUser
from orders.models.goods import Goods, GoodDeal
from orders.permissions import IsAdminOrConsumer
from orders.serializers.goods import GoodsSerializer, GoodDealSerializer


class BaseAPIView(generics.GenericAPIView):
    """
    Базовий клас для представлень, де потрібна перевірка дозволу.
    """

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminUser()]
        return [IsAdminOrConsumer()]


class GoodsListCreate(BaseAPIView, generics.ListCreateAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['created_at', 'count']
    search_fields = ['type', 'drone__name']


class GoodsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    permission_classes = (IsAdminUser,)


class GoodDealListCreate(BaseAPIView, generics.ListCreateAPIView):
    queryset = GoodDeal.objects.all()
    serializer_class = GoodDealSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['created_at', 'count']
    search_fields = ['goods__drone__name']


class GoodDealRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = GoodDeal.objects.all()
    serializer_class = GoodDealSerializer
    permission_classes = (IsAdminUser,)

