from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from checkout.models import Order 


def index(request):
    # Return index page
    return render(request, 'home/index.html')

@login_required
def my_orders(request):
    if request.user.is_authenticated:
        # Fetch orders associated with the user's email
        orders = Order.objects.filter(email=request.user.email) 
    else:
        orders = []  # No orders if user is not authenticated

    return render(request, 'home/my_orders.html', {'orders': orders})
