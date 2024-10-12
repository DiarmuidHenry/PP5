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
        print("CASE 1")
        if cart[unique_key]['option']:
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

# def update_cart(request, item_id):
#     # messages.success(request, f'Updated {product.name} quantity in your cart!')

# def remove_from_cart(request, item_id):
#     # messages.success(request, f'Removed {product.name} from your cart.')
