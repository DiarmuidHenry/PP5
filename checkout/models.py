import uuid
from django.db import models
from django.db.models import JSONField
from products.models import Product
from django.contrib.auth.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
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
    total_co2_footprint = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=0)
    total_product_cost = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=0) 
    total_order_cost = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    order_items = models.JSONField(null=True, blank=True)  # Store product details (without price)

    def _generate_order_number(self):
        # Generate random unique order number for each order
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        # Generate and save order number if it doesn't exist already
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def update_total(self):
        # Calculate total cost using product prices from the Product model
        order_total = 0
        total_co2 = 0
        for item in self.order_items:
            product = Product.objects.get(id=item['product_id'])
            item_total = item['quantity'] * product.price
            order_total += item_total
            # Calculate CO2 impact
            total_co2 += item['quantity'] * product.co2_footprint 

        # Update delivery charge if needed
        if order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_charge = settings.DELIVERY_CHARGE
        else:
            self.delivery_charge = 0

        # Final order total
        self.total_order_cost = order_total + self.delivery_charge
        self.total_co2_impact = total_co2  # Update total CO2 impact
        self.save()

    def __str__(self):
        return self.order_number
