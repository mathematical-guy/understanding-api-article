from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Product, OrderProduct, Order
from .serializers import OrderSerializer, ProductSerializer, OrderProductSerializer
from rest_framework import filters


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'brand']

    @action(detail=True, methods=["GET"], url_path="order-items")
    def order_items(self, request, *args, **kwargs):
        order = self.get_object()
        serializer = OrderProductSerializer(instance=order.product_orders.all(), many=True)
        return Response(serializer.data)
    



class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


   