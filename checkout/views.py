from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from .models import Order
from products.models import Product
from cart.contexts import cart_contents
import stripe

def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY

    stripe_secret_key = settings.STRIPE_SECRET_KEY

    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment.")
        return redirect(reverse('products'))



        if request.method == 'POST':
            order_form = OrderForm(request.POST)
            if order_form.is_valid():
                order = order_form.save(commit=False)
                order_items = []
            
                for cart_item in cart.values():  # cart is a dictionary, so we need to iterate its values
                    item_id = cart_item['item_id']  # Correctly access item_id from the cart item
                    print(f"Fetching product with item_id: {item_id}")  # Debug print
                    order_items.append({
                        'product_id': product.id,
                        'quantity': item_data['quantity'],
                        'price': str(product.price),
                    })
            
                order.order_items = order_items 
                order.update_total() 
                order.save()  

                # Clear the cart from the session
                request.session['cart'] = {}
                messages.success(request, "Your order has been placed successfully!")
                return redirect(reverse('order_confirmation', args=[order.order_number]))
    else:
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

    print("Context data:")
    print(context)

    return render(request, template, context)

def order_confirmation(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    context = {
        'order': order,
    }
    return render(request, 'checkout/order_confirmation.html', context)


# def checkout(request):
#     cart = request.session.get('cart', {})
#     if not cart:
#         messages.error(request, "There's nothing in your bag at the moment")
#         return redirect(reverse('products'))

#     order_form = OrderForm()
#     context = {
#         'order_form': order_form,
#     }

#     print("got to here")

#     return render(request, 'checkout/checkout.html', context)