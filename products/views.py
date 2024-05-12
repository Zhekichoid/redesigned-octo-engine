from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Products
from .forms import ProductForm


# Create your views here.

@login_required
def index(request):
    return render(request,'products/index.html')

@login_required
def staff(request):
    return render(request,'products/staff.html')

@login_required
def orders(request):
    return render(request,'products/orders.html')

@login_required
def products(request):
    items = Products.objects.all()

    context = {
        'items' : items
    }
    return render(request,'products/products.html', context)

@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products-products')
    else:
        form = ProductForm()

    context = {
        'form': form
    }
    return render(request,'products/product_create.html', context)

def product_delete(request, pk):
    item = Products.objects.get(product_id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('products-products')
    return render(request, 'products/product_delete.html')

def product_update(request, pk):
    item = Products.objects.get(product_id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('products-products')
    else:
        form = ProductForm(instance=item)

    context = {
        'form': form
    }

    return render(request, 'products/product_update.html', context)