from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Products, Departments, ProductDepartment
from .forms import ProductForm, DepartmentsForm, OrderForm
from django.contrib.auth.models import User


# Create your views here.

@login_required
def index(request):
    return render(request,'products/index.html')


@login_required
def staff(request):
    current_items = request.user
    itemss = User.objects.exclude(id=current_items.id)

    context = {
        'itemss' : itemss
    }

    return render(request,'staff/staff.html', context)


@login_required
def staff_detail(request, pk):
    items = User.objects.get(id=pk)

    context = {
        'items': items
    }

    return render(request, 'staff/staff_detail.html', context)


@login_required
def orders(request):
        return render(request,'orders/orders.html')



def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orders')
    else:
        form = OrderForm()

    context = {
        'form': form
    }
    return render(request,'orders/orders_create.html', context)


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


@login_required
def product_delete(request, pk):
    item = Products.objects.get(id=pk)
    context = {
        'item' : item   
        }
    if request.method=='POST':
        item.delete()
        return redirect('products-products')
    return render(request, 'products/product_delete.html', context)


@login_required
def product_update(request, pk):
    
    item = Products.objects.get(id=pk)
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



#Departments
@login_required
def departments(request):
    items = Departments.objects.all()

    context = {
        'items' : items
    }

    return render(request,'departments/departments.html', context)


@login_required
def department_create(request):
    if request.method == 'POST':
        form = DepartmentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('departments')
    else:
        form = DepartmentsForm()

    context = {
        'form': form
    }
    return render(request,'departments/departments_create.html', context)


@login_required
def department_detail(request, pk):
    department = Departments.objects.get(id=pk)
    items = department.productdepartment_set.select_related('product')

    context = {
        'department' : department,
        'items': items
    }

    return render(request, 'departments/departments_detail.html', context)
