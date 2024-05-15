from django import forms
from .models import Products, Departments, Order

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Products
        fields = '__all__'

class DepartmentsForm(forms.ModelForm):
    
    class Meta:
        model = Departments
        fields = '__all__'

class OrderForm(forms.ModelForm):
    
    class Meta:
        model = Order
        fields = ("client", "order_type")

