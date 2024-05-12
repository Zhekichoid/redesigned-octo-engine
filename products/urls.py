from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='products-index'),
    path('staff/', views.staff, name='products-staff'),
    path('products/', views.products, name='products-products'),
    path('orders/', views.orders, name='products-orders'),
]