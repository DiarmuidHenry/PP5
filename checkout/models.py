# import uuid
# from django.db import models
# from django.contrib.postgres.fields import JSONField  # Only if using PostgreSQL
# from products.models import Product

# class Order(models.Model):
#     order_number = models.CharField(max_length=32, null=False, editable=False)
#     name = models.CharField(max_length=100, null=False, blank=False)
#     email = models.EmailField(max_length=100, null=False, blank=False)
#     phone_number = models.CharField(max_length=20, null=False, blank=False)
#     address_1 = models.CharField(max_length=100, null=False, blank=False)
#     address_2 = models.CharField(max_length=100, null=True, blank=True)
#     city = models.CharField(max_length=100, null=False, blank=False)
#     county = models.CharField(max_length=100, null=True, blank=True)
#     post_code = models.CharField(max_length=20, null=True, blank=True)
#     country = models.CharField(max_length=60, null=False, blank=False)
#     delivery_charge = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
#     order_datetime = models.DateTimeField(auto_now_add=True)
#     total_order_cost = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
#     order_items = JSONField(null=False, blank=False)  # Product quantities and types stored here

#     def _generate_order_number(self):
#         # Generate random unique order number for each order
#         return uuid.uuid4().hex.upper()

#     def save(self, *args, **kwargs):
#         # Generate and save order number if it doesn't exist already
#         if not self.order_number:
#             self.order_number = self._generate_order_number()
#         super().save(*args, **kwargs)

#     def update_total(self):
#         # Automatically update the total cost, including delivery
#         order_total = sum(item['quantity'] * item['price'] for item in self.order_items)
#         if order_total < settings.FREE_DELIVERY_THRESHOLD:
#             self.delivery_charge = settings.DELIVERY_CHARGE
#         else:
#             self.delivery_charge = 0
#         self.total_order_cost = order_total + self.delivery_charge
#         self.save()

#     def __str__(self):
#         return self.order_number


import uuid
from django.db import models
from django.db.models import JSONField
from products.models import Product

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
        for item in self.order_items:
            product = Product.objects.get(id=item['product_id'])
            item_total = item['quantity'] * product.price
            order_total += item_total

        # Update delivery charge if needed
        if order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_charge = settings.DELIVERY_CHARGE
        else:
            self.delivery_charge = 0

        # Final order total
        self.total_order_cost = order_total + self.delivery_charge
        self.save()

    def __str__(self):
        return self.order_number
