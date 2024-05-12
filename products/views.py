from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Products

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
    return render(request,'products/products.html')
