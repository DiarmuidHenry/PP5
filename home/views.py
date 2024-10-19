from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from checkout.models import Order
from products.models import Product
from django.conf import settings
from .forms import NewsletterSignupForm


def index(request):
    # Return index page
    return render(request, 'home/index.html')

@login_required
def my_orders(request):
    if request.user.is_authenticated:
        # Fetch orders associated with the user's email
        orders = Order.objects.filter(user=request.user) 
    else:
        orders = []  # No orders if user is not authenticated

    return render(request, 'home/my_orders.html', {'orders': orders})


@login_required
@login_required
def order_details(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    # Prepare a list of product details for each item in order_items
    product_details = []
    for item in order.order_items:  
        product = get_object_or_404(Product, id=item['item_id']) 
        
        # Create a new dictionary with the desired details
        product_info = {
            'description': product.description,
            'co2_footårint': product.co2_footprint,
            'option': item['option'],
            'image': product.image,
            'image_url': product.image.url if product.image else '/media/no_image.jpg',
            'item_total': item['price'],  
            'name': product.name,  
            'price': product.price,  
            'quantity': item['quantity'],  
        }
        product_details.append(product_info)  # Append to the list

    context = {
        'order': order,
        'product_details': product_details,
        'free_tote_bag_threshold': settings.FREE_TOTE_BAG_THRESHOLD,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
    }

    return render(request, 'home/order_details.html', context)

def newsletter_signup(request):
    if request.method == 'POST':
        form = NewsletterSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for signing up for our newsletter!')
            return redirect('home')
    else:
        form = NewsletterSignupForm()
    
    return render(request, 'home/index.html', {'form': form})