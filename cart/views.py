from django.shortcuts import render, redirect, get_object_or_404, HttpResponse, reverse
from django.contrib import messages
from products.models import Product

# Create your views here.

def view_cart(request):
    # Return cart and contents
    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    # Adding items to cart

    product = Product.objects.get(pk=item_id)

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
        if cart[unique_key].get('option'):
            messages.success(request, f'Added {product.name} - {cart[unique_key]['option'].title()} to your cart!')
        else:
            messages.success(request, f'Added {product.name} to your cart!')
    else:        
        if selected_option:
            cart[unique_key] = {
                'product_id': product.id,
                'quantity': quantity,
                'option': selected_option,
            }
            messages.success(request, f'Added {product.name} - {cart[unique_key]['option'].title()} to your cart!')
        else:
            cart[unique_key] = {
                'product_id': product.id,
                'quantity': quantity,
            }
            messages.success(request, f'Added {product.name} to your cart!')


    request.session['cart'] = cart
    return redirect(redirect_url)

def adjust_cart(request, item_id):
    # Adjusting quantities to cart

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    selected_option = request.POST.get('option')
    cart = request.session.get('cart', {})

    if selected_option != None:
        unique_key = f"{item_id}--{selected_option}"
    else:
        unique_key = str(item_id)


    if unique_key in cart:
        cart[unique_key]['quantity'] = quantity  # Update the quantity

    if quantity > 0:
        # Update the cart
        cart[unique_key]['quantity'] = quantity  # Update the quantity
    else:
        del cart[unique_key]
        
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

def remove_from_cart(request, item_id):

    selected_option = request.POST.get('option')
    cart = request.session.get('cart', {})

    try:

        if selected_option != "None":
            unique_key = f"{item_id}--{selected_option}"
        else:
            unique_key = str(item_id)

        del cart[unique_key]
            
        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
