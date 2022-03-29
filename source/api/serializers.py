from rest_framework import serializers

from webapp.models import Basket, Product, Order, OrderBasketProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category', 'remainder', 'price']
        read_only_fields = ['id']

class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderBasketProduct
        fields = ('id', 'order_id', 'product_id', 'amount')

class OrderSerializer(serializers.ModelSerializer):
    orderbasket = OrderProductSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = ('id', 'date', 'name', 'phone', 'address', 'orderbasket')
        read_only_fields = ('date', )