from django.shortcuts import render

from rest_framework import viewsets

from api.serializers import ProductSerializer, OrderSerializer
from webapp.models import Product, Order, OrderBasketProduct


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
   queryset = Order.objects.all()
   serializer_class = OrderSerializer

