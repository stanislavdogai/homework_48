from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView

from webapp.models import Product
from webapp.forms import ProductForm, DeleteProductForm
from webapp.views.base import SearchView


class ProductIndexView(SearchView):
    model = Product
    context_object_name = 'products'
    template_name = 'products/index.html'
    paginate_by = 5
    search_fields = ['name__icontains']
    ordering = 'name'


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
