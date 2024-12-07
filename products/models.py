from django.db import models
from django.conf import settings
from django.db.models import Avg
from django.core.validators import MinValueValidator, MaxValueValidator, DecimalValidator
from cloudinary.models import CloudinaryField


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='subcategories')

    def __str__(self):
        if self.parent:
            return f"{self.parent.name} - {self.name}".title()  # "Parent - Product"
        else:
            return self.name  # Just "Category"

# Details of the products in the shop
class Product(models.Model):
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=100, null=True, blank=True)
    image = CloudinaryField(
        'image', 
        default='https://res.cloudinary.com/drrywrvwv/image/upload/v1729274738/background_small_uxkai1.jpg'
    )
    description = models.TextField()
    price = models.DecimalField(max_digits=10, validators=[MinValueValidator(0.01)], decimal_places=2)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    co2_footprint = models.FloatField()
    stock = models.IntegerField()
    options = models.TextField(null=True, blank=True)  # Comma separated string

    def get_options_list(self):
        return self.options.split(',') if self.options else []

    # Create rating from mean of relevant entries in Rating
    @property
    def average_rating(self):
        average = Rating.objects.filter(product=self).aggregate(Avg('rating'))['rating__avg']
        return round(average, 2) if average is not None else 0

    def __str__(self):
        return self.name

# Allow users to rate products
class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f'{self.product.name}: {self.rating} by {self.user.email}'

    # Only allow 1 rating per item per person
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'product'], name='unique_user_product_rating'
                )
        ]

