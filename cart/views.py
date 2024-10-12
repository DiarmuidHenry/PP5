from django.shortcuts import render, redirect, get_object_or_404, HttpResponse, reverse
from django.contrib import messages
from products.models import Product

# Create your views here.

def view_cart(request):
    # Return cart and contents
    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):

    print("request:")
    print(request)

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
    # messages.success(request, f'Updated {product.name} quantity in your cart!')
    # Adjusting quantities to cart

    print("arrived at adjust_cart")

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    print(quantity)
    selected_option = request.POST.get('option')
    print("selected_option:")
    print(selected_option)
    cart = request.session.get('cart', {})


    if selected_option != None:
        print("2")
        unique_key = f"{item_id}--{selected_option}"
    else:
        print("3")
        unique_key = str(item_id)

    print("Attempting to adjust cart with unique_key:", unique_key)
    print(type(unique_key))

    if unique_key in cart:
        cart[unique_key]['quantity'] = quantity  # Update the quantity
    else:
        print(f"Key {unique_key} not found in cart.")


    if quantity > 0:
        # Update the cart
        cart[unique_key]['quantity'] = quantity  # Update the quantity
    else:
        del cart[unique_key]
        
        
    # # BUG FIX: Check if there is an incorrect entry (without option) for the same product and remove it
    # base_key = str(item_id)  # Key without an option
    # if base_key in cart and unique_key != base_key:
    #     print("8")
    #     # Remove the incorrect entry without the option if it exists
    #     cart.pop(base_key, None)

    # if unique_key in cart:
    #     cart[unique_key]['quantity'] += quantity
    #     print("CASE 1")
    #     if cart[unique_key]['option']:
    #         messages.success(request, f'Added {product.name} - {cart[unique_key]['option'].title()} to your cart!')
    #     else:
    #         messages.success(request, f'Added {product.name} to your cart!')
    # else:        
    #     if selected_option:
    #         cart[unique_key] = {
    #             'product_id': product.id,
    #             'quantity': quantity,
    #             'option': selected_option,
    #         }
    #         messages.success(request, f'Added {product.name} - {cart[unique_key]['option'].title()} to your cart!')
    #     else:
    #         cart[unique_key] = {
    #             'product_id': product.id,
    #             'quantity': quantity,
    #         }
    #         messages.success(request, f'Added {product.name} to your cart!')


    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

def remove_from_cart(request, item_id):
    print("Got to remove_from_cart")
    # messages.success(request, f'Removed {product.name} from your cart.')

    selected_option = request.POST.get('option')
    cart = request.session.get('cart', {})
    print("1")
    print(selected_option)
    print(type(selected_option))

    try:

        if selected_option != "None":
            print("2")
            unique_key = f"{item_id}--{selected_option}"
        else:
            print("3")
            unique_key = str(item_id)

        del cart[unique_key]
            
        
        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
