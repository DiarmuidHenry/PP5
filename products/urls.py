from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_id>', views.product_detail, name='product_detail'),
    path('rate/<int:product_id>/', views.rate_product, name='rate_product'),
    path('product_management/', views.product_management, name='product_management'),


]
