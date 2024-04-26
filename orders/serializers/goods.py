from rest_framework import serializers

from orders.models.goods import Goods, GoodDeal


class GoodsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        exclude = ['created_at', 'updated_at']


class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = '__all__'


class GoodDealSerializer(serializers.ModelSerializer):
    # status = serializers.CharField(source='get_status_display')
    # type = serializers.CharField(source='get_type_display')

    goods = GoodsDetailSerializer()

    class Meta:
        model = GoodDeal
        fields = '__all__'
