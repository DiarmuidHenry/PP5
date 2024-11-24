from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, Rating
from .forms import ProductForm
from django.contrib.auth.decorators import login_required, user_passes_test

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

def product_detail(request, product_id):
    # Show details of a single product
    product = get_object_or_404(Product, pk=product_id)
    user_rating = Rating.objects.filter(product=product, user=request.user).first() if request.user.is_authenticated else None

    context = {
        'product': product,
        'user_rating': user_rating,
    }
    return render(request, 'products/product_detail.html', context)

@login_required
def product_management(request):
    if request.user.is_superuser:
        print("Got to here")
        products = Product.objects.all()
        print("Product loaded")
        return render(request, 'products/product_management.html', {'products': products})
    else:
        print("not registering superuser")
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('home')

@user_passes_test(lambda u: u.is_superuser)
def view_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/view_product.html', context)

@user_passes_test(lambda u: u.is_superuser)
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect('product_management')
    else:
        form = ProductForm(instance=product)

    return render(request, 'products/edit_product.html', {'form': form, 'product': product})

@user_passes_test(lambda u: u.is_superuser)
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully!')
        return redirect('product_management')  # Redirect to product management page

    return render(request, 'products/delete_product.html', {'product': product})

@user_passes_test(lambda u: u.is_superuser)
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully!')
            return redirect('product_management')  # Redirect to product management page
    else:
        form = ProductForm()

    return render(request, 'products/add_product.html', {'form': form})