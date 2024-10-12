import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings

# Create your models here.

class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    address_1 = model.CharField(max_length=100, null=False, blank=False)
    address_2 = model.CharField(max_length=100, null=True, blank=True)
    city = model.CharField(max_length=100, null=False, blank=False)
    county = model.CharField(max_length=100, null=True, blank=True)
    post_code = model.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=60, null=False, blank=False)
    order_datetime = models.DateTimeField(auto_now_add=True)
    total_order_cost = models.DecimalField(max_digits=10, decimal_places=s, null=False, blank=False)

class OrderItem(models.Model):
    order_number = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    # Only consider subcategories in product_option
    product_option = models.ForeignKey(Category, null=False, blank=False, on_delete=models.CASCADE, limit_choices_to={'parent__isnull': False})
    quantity = models.IntegerField(null=False, blank=False, default=0)
    item_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, editable=False)


    