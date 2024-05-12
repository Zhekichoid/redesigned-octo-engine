from django.db import models

# Create your models here.

class Departments(models.Model):
    
    deparment_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    capacity = models.DecimalField(max_digits=10, decimal_places=2)
    available_space = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = 'Departments'
    
    def __str__(self) -> str:
        return self.name

class Products(models.Model):
    
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=60)
    amount = models.IntegerField()
    
    class Meta:
        verbose_name_plural = 'Products'
    
    def __str__(self) -> str:
        return self.name

class ProductDepartment(models.Model):
    
    """Product-department connection."""
    class Meta:
        unique_together = (('department', 'product'),)

    department = models.ForeignKey(Departments, on_delete=models.CASCADE) 
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    amount = models.IntegerField()
    