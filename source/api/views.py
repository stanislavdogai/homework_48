from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS, AllowAny, DjangoModelPermissions, IsAdminUser

from api.serializers import ProductSerializer, OrderSerializer
from webapp.models import Product, Order


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return []
        return [DjangoModelPermissions()]



class OrderViewSet(viewsets.ModelViewSet):
   queryset = Order.objects.all()
   serializer_class = OrderSerializer
   permission_classes = [IsAdminUser, DjangoModelPermissions]

   def get_permissions(self):
       if self.request.method in ['POST']:
           return []
       return [DjangoModelPermissions()]

