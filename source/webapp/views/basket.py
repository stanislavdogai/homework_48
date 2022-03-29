from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.contrib.sessions.models import Session


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
        my_dict = request.session.get('my_dict')
        if not my_dict:
            request.session['my_dict'] = {}
        product = Product.objects.get(pk=kwargs.get('pk'))
        count = request.POST.get('quantity')
        if count == '':
            count = 1
        count = int(count)
        print(my_dict.keys())
        print(str(product.pk) in my_dict.keys())
        if str(product.pk) in my_dict.keys():
            print('elif')
            # basket = Basket.objects.get(product_id=product.pk)
            # if product.remainder == basket.amount:
            #     return render(request, 'basket/error.html')
            # else:
            #     basket = Basket.objects.get(product_id=product.pk)
            #     basket.amount += int(count)
            my_dict[str(product.pk)] += count
                # request.session[product.pk]
                # print(ses)
                # basket.save()
            print(my_dict)
        else:
            amount = 1
            Basket.objects.create(product=product, amount=count)
            my_dict[str(product.pk)] = count
            print(my_dict)
        request.session['my_dict'] = my_dict
        return redirect('webapp:product_index')

class BasketProductDelete(View):
    def get(self, request, *args, **kwargs):
        # request.session['key'] = value
        basket = get_object_or_404(Basket, pk=kwargs.get('pk'))
        if basket.amount > 1:
            basket.amount -= 1
            basket.save()
        else:
            basket.delete()
        return redirect('webapp:basket')

class BasketProductRemove(View):
    def get(self, request, *args, **kwargs):
        basket = get_object_or_404(Basket, pk=kwargs.get('pk'))
        basket.delete()
        return redirect('webapp:basket')
