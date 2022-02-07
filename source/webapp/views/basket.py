from django.shortcuts import get_object_or_404, render, redirect
from django.views import View

from webapp.models import Product, Basket


class BasketView(View):
    def get(self, request, *args, **kwargs):
        basket = Basket.objects.all()
        return render(request, 'basket/index.html', {'basket':basket})

class ProductAddBasket(View):
    def post(self, request, *args, **kwargs):
        product = Product.objects.get(pk=kwargs.get('pk'))
        print(product)
        # basket = get_object_or_404(Basket, product_id=kwargs.get('pk'))
        # print(basket)
        Basket.objects.create(product=product, amount=1)
        # basket = basket.amount + 1
        # print(f'amount = {basket}')
        # check = Basket.objects.update()
        # print(check)
        # print(basket.product, basket.amount)
        return redirect('product_index')

class BasketProductDelete(View):
    def get(self, request, *args, **kwargs):
        product = get_object_or_404(Basket, pk=kwargs.get('pk'))
        print(product)
        product.delete()
        return redirect('basket')
