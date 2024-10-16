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

    print("HERE 1")

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
                    print("ASSIGNED USER - BUG TEST")

                print("Cart info:")
                print(cart_info)
            
                for item in cart_info['cart_items']:
                    print("item")
                    print(item)
                    item_id = item['item_id']
                    print("item_id")
                    print(item_id)
                    quantity = item['quantity']
                    print("quantity")
                    print(quantity)
                    price = float(item['item_total']) 
                    print("price")
                    print(price)
                    option = item['option']
                    print("option (if exists):")
                    print(option)
                    print()
                    print()
                    
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









    # cart = request.session.get('cart', {})
    # if not cart:
    #     messages.error(request, "There's nothing in your cart at the moment.")
    #     return redirect(reverse('products'))

    # if request.method == 'POST':
    #     print("POST")
    #     order_form = OrderForm(request.POST)
    #     if order_form.is_valid():
    #         order = order_form.save(commit=False)
    #         order_items = []
        
    #         for cart_item in cart.values():  # cart is a dictionary, so we need to iterate its values
    #             item_id = cart_item['item_id']  # Correctly access item_id from the cart item
    #             print(f"Fetching product with item_id: {item_id}")  # Debug print
    #             order_items.append({
    #                 'product_id': product.id,
    #                 'quantity': item_data['quantity'],
    #                 'price': str(product.price),
    #             })
        
    #         order.order_items = order_items 
    #         order.update_total() 
    #         order.save()  

    #         # Clear the cart from the session
    #         request.session['cart'] = {}
    #         messages.success(request, "Your order has been placed successfully!")
    #         return redirect(reverse('order_confirmation', args=[order.order_number]))
    # else:
    #     order_form = OrderForm()
    
    order_form = OrderForm()

    print("NOT POST")

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
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order confirmed! \
        You will soon receive confirmation of Order {order_number} at {order.email}.')

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
