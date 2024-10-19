from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from .models import Order
from products.models import Product
from cart.contexts import cart_contents
from django.contrib.auth.decorators import login_required
import stripe

def checkout(request):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'address_1': request.POST['address_1'],
            'address_2': request.POST['address_2'],
            'city': request.POST['city'],
            'county': request.POST['county'],
            'post_code': request.POST['post_code'],
            'country': request.POST['country'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            try:
                # Create order instance, but don't save to DB yet
                order = order_form.save(commit=False)
                cart_info = cart_contents(request)
                order.total_product_cost = cart_info['subtotal']
                order.delivery_charge = cart_info['delivery_charge']
                order.total_order_cost = cart_info['total']
                order.total_co2_footprint = cart_info['total_co2_footprint']
                order_items = []

                # Assign the logged-in user to the order, if authenticated
                if request.user.is_authenticated:
                    order.user = request.user
            
                for item in cart_info['cart_items']:
  
                    item_id = item['item_id']
                    quantity = item['quantity']
                    price = float(item['item_total']) 
                    option = item['option']
                    
                    order_items.append({
                        'item_id': item_id,
                        'option': option,
                        'quantity': quantity,
                        'price': price,
                    })
                
                order.order_items = order_items
                
                order.save()
            
            except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your cart wasn't found in our database. "
                        "Please contact us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_cart'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('order_confirmation', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "There is currently nothing in your cart.")
            return redirect(reverse('products'))
    
    order_form = OrderForm()

    product_count = sum(item['quantity'] for item in cart.values())

    # Fetch product details for each item in the cart
    products = {}
    for item in cart.values():
        product_id = item['product_id']
        try:
            product = Product.objects.get(id=product_id)
            products[product_id] = product
        except Product.DoesNotExist:
            products[product_id] = None

    current_cart = cart_contents(request)
    total = current_cart['total']
    stripe_total = round(total*100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    if not stripe_public_key:
        message.warning(request, "Stripe public key is missing!")

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret
    }

    return render(request, template, context)

def order_confirmation(request, order_number):
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order confirmed! \
        Order Number: {order_number}')

    if 'cart' in request.session:
        del request.session['cart']

    context = {
        'order': order,
    }
    return render(request, 'checkout/order_confirmation.html', context) 

@login_required
def my_orders(request):
    # Retrieve orders for the logged-in user
    orders = Order.objects.filter(email=request.user.email)

    context = {
        'orders': orders,
    }
    return render(request, 'orders/my_orders.html', context)
