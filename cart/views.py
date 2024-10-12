from django.shortcuts import render, redirect, get_object_or_404, HttpResponse, reverse
from django.contrib import messages
from products.models import Product

# Create your views here.

def view_cart(request):
    # Return cart and contents
    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    # Adding items to cart

    product = get_object_or_404(Product, pk=item_id)

    quantity = int(request.POST.get('quantity'))

    redirect_url = request.POST.get('redirect_url')

    selected_option = request.POST.get('product_option')

    cart = request.session.get('cart', {})

    if 'product_option' in request.POST:
        selected_option = request.POST.get('product_option')
        unique_key = f"{item_id}--{selected_option}"
    else:
        unique_key = str(item_id)

    if unique_key in cart:
        cart[unique_key]['quantity'] += quantity
    else:
        if selected_option:
            cart[unique_key] = {
                'product_id': product.id,
                'quantity': quantity,
                'option': selected_option,
            }
        else:
            cart[unique_key] = {
                'product_id': product.id,
                'quantity': quantity,
            }


    request.session['cart'] = cart
    return redirect(redirect_url)