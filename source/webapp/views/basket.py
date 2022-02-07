from django.shortcuts import get_object_or_404, render, redirect
from django.views import View

from webapp.forms import OrderBasketForm
from webapp.models import Product, Basket, Order, OrderBasketProduct


class BasketView(View):
    def get(self, request, *args, **kwargs):
        basket = Basket.objects.filter(product__remainder__gt=0)
        form = OrderBasketForm()
        sum = 0
        for price in basket:
            sum += (price.product.price * price.amount)
        return render(request, 'basket/index.html', {'basket':basket, 'form':form, 'sum':sum})

    def post(self, request, *args, **kwargs):
        products_basket = Basket.objects.all()
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        order = Order.objects.create(name=name, phone=phone, address=address)
        for basket in products_basket:
            product = Product.objects.get(pk=basket.product.pk)
            OrderBasketProduct.objects.create(product_id=product.pk, amount=basket.amount, order=order)
            product.remainder -= basket.amount
            product.save()
            basket.delete()
        return render(request, 'basket/thank.html')

class ProductAddBasket(View):
    def post(self, request, *args, **kwargs):
        product = Product.objects.get(pk=kwargs.get('pk'))
        if Basket.objects.filter(product_id=product.pk):
            basket = Basket.objects.get(product_id=product.pk)
            if product.remainder == basket.amount:
                return render(request, 'basket/error.html')
            else:
                basket = Basket.objects.get(product_id=product.pk)
                basket.amount += 1
                basket.save()
        else:
            Basket.objects.create(product=product, amount=1)
        return redirect('product_index')

class BasketProductDelete(View):
    def get(self, request, *args, **kwargs):
        product = get_object_or_404(Basket, pk=kwargs.get('pk'))
        product.delete()
        return redirect('basket')
