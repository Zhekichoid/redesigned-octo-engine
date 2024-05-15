from django.db import models

# Create your models here.

ORDER_TYPE_CHOICES = (
    ('incoming', 'incoming'),
    ('outgoing', 'outgoing'),
)

class Departments(models.Model):
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    capacity = models.DecimalField(max_digits=10, decimal_places=2)
    available_space = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = 'Departments'
    
    def __str__(self) -> str:
        return self.name

class Products(models.Model):
    
    id = models.AutoField(primary_key=True)
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
    
class Order(models.Model):

    id = models.AutoField(primary_key=True)
    client = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    status = models.CharField(max_length=30)
    order_type = models.CharField(max_length=10, choices=ORDER_TYPE_CHOICES, default='outgoing')

    def __str__(self) -> str:
        return self.id

class ProductOrder(models.Model):
    """Product-order connection."""
    class Meta:
        unique_together = (('order', 'product'),)

    order = models.ForeignKey(Order, on_delete=models.CASCADE) 
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()