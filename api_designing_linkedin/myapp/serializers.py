from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import Product, Order, OrderProduct


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class OrderProductSerializer(ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = OrderProduct
        fields = "__all__"




class OrderSerializer(ModelSerializer):
    order_products = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = "__all__"


    def get_order_products(self, order: Order):
        print(order, order.order_products.all())
        return OrderProductSerializer(instance=order.order_products.all(), many=True).data
        return 1