from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='products-index'),
    
    path('staff/', views.staff, name='products-staff'),
    path('staff/detail/<int:pk>/', views.staff_detail, name='products-staff-detail'),
    
    path('products/', views.products, name='products-products'),
    path('products/create/', views.product_create, name='products-create'),
    path('products/delete/<int:pk>/', views.product_delete,
        name='products-delete'),
    path('products/update/<int:pk>/', views.product_update,
        name='products-update'),
   
    path('departments/', views.departments, name='departments'),
    path('departments/create/', views.department_create, name='departments-create'),
    path('departments/detail/<int:pk>/', views.department_detail, name='departments-detail'),


    path('orders/', views.orders, name='orders'),
    path('orders/create/', views.order_create, name='orders-create'),

]