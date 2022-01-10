from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Product
from webapp.forms import ProductForm, DeleteProductForm




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

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        form = DeleteProductForm()
        return render(request, 'delete.html', {'product' : product, 'form' : form})
    else:
        form = DeleteProductForm(data=request.POST)
        if form.is_valid():
            if form.cleaned_data.get('name') != product.name:
                form.errors['name'] = ['Название продукта не соответствует']
                return render(request, 'delete.html', {'product' : product, 'form' : form})
            product.delete()
            return redirect('home_page')
        return render(request, 'delete.html', {'product': product, 'form': form})

def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        form = ProductForm(initial={
            'name': product.name,
            'category': product.category,
            'description': product.description,
            "remainder": product.remainder,
            "price": product.price
        })
        return render(request, 'update.html', {"product": product, "form": form})
    else:
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product.name = form.cleaned_data.get('name')
            product.category = form.cleaned_data.get('category')
            product.description = form.cleaned_data.get('description')
            product.remainder = form.cleaned_data.get('remainder')
            product.price = form.cleaned_data.get('price')
            product.save()
            return redirect("product_view", pk=product.pk)
        return render(request, 'update.html', {"product": product, "form": form})