from django.contrib import admin
from .models import Products, Departments, ProductDepartment, Order, ProductOrder

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'amount')

class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity', 'available_space')

class ProductDepartmentAdmin(admin.ModelAdmin):
    list_display = ('product', 'department', 'amount')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
     list_display = ('id', 'order_type', 'client', 'datetime', 'status')

@admin.register(ProductOrder)
class ProductOrderAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'amount')



# Register your models here.
admin.site.register(Products, ProductsAdmin)

admin.site.register(Departments, DepartmentsAdmin)

admin.site.register(ProductDepartment, ProductDepartmentAdmin)