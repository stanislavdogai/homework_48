from django.shortcuts import render, get_object_or_404
from webapp.models import Product
# Create your views here.
def home_page(request):
    products = Product.objects.order_by('name')
    return render(request, 'index.html', {'products' : products})

def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product' : product}
    return render(request, 'product_view.html', context)