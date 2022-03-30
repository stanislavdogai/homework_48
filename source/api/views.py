from http import HTTPStatus

from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS, AllowAny, DjangoModelPermissions, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import ProductSerializer, OrderSerializer, BasketSerializer
from webapp.models import Product, Order, Basket


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return []
        return [IsAuthenticated(), DjangoModelPermissions()]



class OrderViewSet(viewsets.ModelViewSet):
   queryset = Order.objects.all()
   serializer_class = OrderSerializer
   permission_classes = [IsAdminUser, DjangoModelPermissions]

   def get_permissions(self):
       if self.request.method in ['POST']:
           return []
       return [IsAdminUser(), DjangoModelPermissions()]

class BasketAddAPIView(APIView):
    def post(self, request, *args, **kwargs):
        basket_serializer = BasketSerializer(data=request.data)
        try:
            if request.data['amount'] == '0':
                request.data['amount'] = 1
            if Basket.objects.filter(product_id=request.data['product']):
                basket = Basket.objects.get(product_id=request.data['product'])
                basket.amount += int(request.data['amount'])
                basket_serializer = BasketSerializer(data={"product" : request.data['product'], "amount" : basket.amount}, instance=basket)
                basket_serializer.is_valid(raise_exception=True)
                basket_serializer.save()
                return Response(basket_serializer.data, status=HTTPStatus.OK)
            else:
                basket_serializer.save()
                return Response(basket_serializer.data, status=HTTPStatus.CREATED)
        except ValidationError as err:
            return Response(data=err.detail, status=HTTPStatus.BAD_REQUEST)

class BasketProductDelete(APIView):
    def delete(self, request, *args, **kwargs):
        basket = Basket.objects.get(product_id=request.data['product'])
        if basket.amount > 1:
            basket.amount -= 1
            basket_serializer = BasketSerializer(data={"product" : request.data['product'], "amount" : basket.amount}, instance=basket)
            basket_serializer.is_valid(raise_exception=True)
            basket_serializer.save()
            return Response(data={'message' : 'Удаление прошло успешно'}, status=204)
        else:
            return Response(data={'err' : 'Нечего удалять'}, status=HTTPStatus.BAD_REQUEST)

class BasketProductRemove(APIView):
    def delete(self, request, *args, **kwargs):
        basket = Basket.objects.get(product_id=request.data['product'])
        basket.delete()
        return Response(data={'message' : 'Удаление прошло успешно'}, status=204)

class BasketList(APIView):
    def get(self, request, *args, **kwargs):
        baskets = Basket.objects.all()
        serializer = BasketSerializer(baskets, many=True)
        return Response(serializer.data)