from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Product
from webapp.forms import ProductForm
# Create your views here.
def home_page(request):
    products = Product.objects.order_by('name')
    return render(request, 'index.html', {'products' : products})

def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product' : product}
    return render(request, 'product_view.html', context)

def create_product(request):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'create.html', {'form' : form})
    else:
        form = ProductForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            description = form.cleaned_data.get('description')
            category = form.cleaned_data.get('category')
            price = form.cleaned_data.get('price')
            remainder = form.cleaned_data.get('remainder')
            new_product = Product.objects.create(name=name,description=description,category=category,price=price,remainder=remainder)
            return redirect('product_view', pk=new_product.pk)
        return render(request, 'create.html', {'form' : form})