from django.contrib import admin
from .models import Products, Departments, ProductDepartment

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'amount')

class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity', 'available_space')

class ProductDepartmentAdmin(admin.ModelAdmin):
    list_display = ('product', 'department', 'amount')

# Register your models here.
admin.site.register(Products, ProductsAdmin)

admin.site.register(Departments, DepartmentsAdmin)
admin.site.register(ProductDepartment, ProductDepartmentAdmin)