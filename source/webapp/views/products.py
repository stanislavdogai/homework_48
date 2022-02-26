from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView

from webapp.models import Product
from webapp.forms import ProductForm
from webapp.views.base import SearchView


class ProductIndexView(SearchView):
    model = Product
    context_object_name = 'products'
    template_name = 'products/index.html'
    paginate_by = 6
    search_fields = ['name__icontains']
    ordering = 'name'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.exclude(remainder=0)
        return queryset.order_by('name', 'category')



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
    success_url = reverse_lazy('webapp:product_index')



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


