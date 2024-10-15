from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, Rating
from django.contrib.auth.decorators import login_required

# Create your views here.

def all_products(request):

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if sortkey == 'rating':
                products = products.annotate(average_rating=Avg('ratings__rating'))
                sortkey = 'average_rating'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}' # Reverse direction
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter search criteria and try again.")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'current_categories': categories,
        'current_sorting': current_sorting,
        'products': products,
        'search_term': query,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    # Show details of a single product

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    print("context in details")
    print(context)

    return render(request, 'products/product_detail.html', context)

@login_required
def rate_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        rating_value = request.POST.get('rating')
        
        # Check if the user has already rated the product
        existing_rating = Rating.objects.filter(user=request.user, product=product).first()

        if existing_rating:
            # Update existing rating
            existing_rating.rating = rating_value
            existing_rating.save()
        else:
            # Create a new rating
            Rating.objects.create(user=request.user, product=product, rating=rating_value)

    # Redirect back to the product details page
    return redirect('product_detail', product_id=product.id)

@login_required
def product_detail(request, product_id):
    # Show details of a single product
    product = get_object_or_404(Product, pk=product_id)
    user_rating = Rating.objects.filter(product=product, user=request.user).first() if request.user.is_authenticated else None

    context = {
        'product': product,
        'user_rating': user_rating,
    }
    return render(request, 'products/product_detail.html', context)