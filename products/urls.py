from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('rate/<int:product_id>/', views.rate_product, name='rate_product'),
    path('<product_id>', views.product_detail, name='product_detail'),
    path('product-management/', views.product_management, name='product_management'),
    path('view/<int:product_id>/', views.view_product, name='view_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('add/', views.add_product, name='add_product'),
]