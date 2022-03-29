from rest_framework import serializers

from webapp.models import Basket, Product, Order


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = ['amount', 'product',]

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'remainder', 'price']
        read_only_fields = []

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['name', 'phone', 'address', 'date']
        read_only_fields = ['date']

