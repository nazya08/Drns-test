from django.urls import path

from orders.views import orders, goods


app_name = 'orders'


# orders
urlpatterns = [
    path('order-list/', orders.OrderListCreate.as_view(), name='order-list'),
    path('<uuid:pk>/', orders.OrderRetrieveUpdateDestroy.as_view(), name='order-detail'),
]

# goods
urlpatterns += [
    path('goods-list/', goods.GoodsListCreate.as_view(), name='order-list'),
    path('goods/<int:pk>/', goods.GoodsRetrieveUpdateDestroy.as_view(), name='order-detail'),
]

# good-deals
urlpatterns += [
    path('good-deal-list/', goods.GoodDealListCreate.as_view(), name='order-list'),
    path('good-deal/<uuid:pk>/', goods.GoodDealRetrieveUpdateDestroy.as_view(), name='order-detail'),
]
