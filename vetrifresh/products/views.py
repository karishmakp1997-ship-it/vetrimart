from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import Category, Product

def shop(request):
    categories = Category.objects.filter(is_active=True).order_by('order')
    products = Product.objects.filter(is_active=True)
    
    # Category filter
    category_slug = request.GET.get('category')
    selected_category = None
    if category_slug:
        selected_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=selected_category)
    
    # Price filter
    min_price = request.GET.get('min_price', 0)
    max_price = request.GET.get('max_price', 10000)
    products = products.filter(price__gte=min_price, price__lte=max_price)
    
    # Rating filter
    rating = request.GET.get('rating')
    if rating:
        products = products.filter(rating__gte=rating)
    
    # Sorting
    sort = request.GET.get('sort', 'latest')
    if sort == 'latest':
        products = products.order_by('-created_at')
    elif sort == 'price_low':
        products = products.order_by('price')
    elif sort == 'price_high':
        products = products.order_by('-price')
    elif sort == 'rating':
        products = products.order_by('-rating')
    
    # Pagination
    paginator = Paginator(products, 12)
    page = request.GET.get('page', 1)
    products = paginator.get_page(page)
    
    context = {
        'categories': categories,
        'products': products,
        'selected_category': selected_category,
        'sort': sort,
        'min_price': min_price,
        'max_price': max_price,
    }
    return render(request, 'products/shop.html', context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    related = Product.objects.filter(
        category=product.category, 
        is_active=True
    ).exclude(id=product.id)[:4]
    
    context = {
        'product': product,
        'related_products': related,
    }
    return render(request, 'products/product_detail.html', context)

def add_to_cart(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        cart = request.session.get('cart', {})
        key = str(product_id)
        cart[key] = cart.get(key, 0) + 1
        request.session['cart'] = cart
        request.session.modified = True
        cart_count = sum(cart.values())
        return JsonResponse({
            'success': True, 
            'cart_count': cart_count,
            'message': f'{product.name} added to cart!'
        })
    return JsonResponse({'success': False})

def get_cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    for product_id, qty in cart.items():
        try:
            product = Product.objects.get(id=product_id)
            subtotal = product.price * qty
            total += subtotal
            cart_items.append({
                'id': product.id,
                'name': product.name,
                'price': str(product.price),
                'unit': product.unit,
                'quantity': qty,
                'subtotal': str(subtotal),
                'image': product.image.url if product.image else '',
            })
        except Product.DoesNotExist:
            pass
    return JsonResponse({'items': cart_items, 'total': str(total)})

def remove_from_cart(request, product_id):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        key = str(product_id)
        if key in cart:
            del cart[key]
            request.session['cart'] = cart
            request.session.modified = True
        cart_count = sum(cart.values())
        return JsonResponse({'success': True, 'cart_count': cart_count})
    return JsonResponse({'success': False})