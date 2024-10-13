import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from products.models import Product, Category

# Create your models here.

class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    address_1 = models.CharField(max_length=100, null=False, blank=False)
    address_2 = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=False, blank=False)
    county = models.CharField(max_length=100, null=True, blank=True)
    post_code = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=60, null=False, blank=False)
    delivery_charge = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    order_datetime = models.DateTimeField(auto_now_add=True)
    total_order_cost = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)

    def _generate_order_number(self):
    # Generate random unique order number for each order
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
    # Generate and save order number if it doesn't exist already
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)
    
    def update_total(self):
    # Automatically update current order cost
        self.total_order_cost = self.orderlineitems.aggregate(Sum('item_total'))['item_total__sum']
        if self.total_order_cost < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_charge = settings.FREE_DELIVERY_THRESHOLD
        else:
            self.delivery_charge = 0
        self.total_order_cost = self_order_total + self.delivery_charge
        self.save()

    def __str__(self):
        return self.order_number 

class OrderItem(models.Model):
    order_number = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    # Only consider subcategories in product_option
    product_option = models.ForeignKey(Category, null=False, blank=False, on_delete=models.CASCADE, limit_choices_to={'parent__isnull': False})
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        # Create itemline total
        self.item_total = self.quantity * self.product.price 
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.product} {self.product_option} - Order # {self.order_number}'


    