from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView

from webapp.models import Product, Basket
from webapp.forms import ProductForm, DeleteProductForm
from webapp.views.base import SearchView


class ProductIndexView(SearchView):
    model = Product
    context_object_name = 'products'
    template_name = 'products/index.html'
    paginate_by = 6
    search_fields = ['name__icontains']
    ordering = 'name'

    def get_queryset(self):
        return Product.objects.filter(remainder__gt=0)



class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/create.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_view.html'


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/delete.html'
    success_url = reverse_lazy('product_index')



class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/update.html'

class ProductBusketView(View):
    def get(self, request, *args, **kwargs):
        print(request)
        product = get_object_or_404(Product, pk=kwargs.get('pk'))

        print(product.remainder)
        print(kwargs)
        return render(request, 'products/index.html', {'product' : product})


