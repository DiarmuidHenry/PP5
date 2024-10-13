from django import template
from products.models import Product  

register = template.Library()

@register.filter
def get_product_name(item_id):
    try:
        product = Product.objects.get(id=item_id)
        return product.name 
    except Product.DoesNotExist:
        return "Unknown Product"  
