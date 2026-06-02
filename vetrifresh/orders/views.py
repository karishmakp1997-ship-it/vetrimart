from django.shortcuts import render, redirect
from .models import CartItem
from products.models import Product



def get_session_id(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key

def cart_page(request):
    session_id = get_session_id(request)
    items = CartItem.objects.filter(session_id=session_id)

    subtotal = sum([item.subtotal() for item in items])
    shipping = 0
    total = subtotal + shipping

    return render(request, 'orders/cart.html', {
        'items': items,
        'subtotal': subtotal,
        'total': total
    })

def add_to_cart(request, product_id):
    session_id = get_session_id(request)
    product = Product.objects.get(id=product_id)

    qty = int(request.GET.get('qty', 1))  # 👈 get quantity

    item, created = CartItem.objects.get_or_create(
        session_id=session_id,
        product=product
    )

    if not created:
        item.quantity += qty
    else:
        item.quantity = qty

    item.save()

    return redirect('cart')


def remove_from_cart(request, product_id):
    session_id = get_session_id(request)
    CartItem.objects.filter(
        session_id=session_id,
        product_id=product_id
    ).delete()

    return redirect('cart')


def update_quantity(request, product_id, action):
    session_id = get_session_id(request)
    item = CartItem.objects.get(session_id=session_id, product_id=product_id)

    if action == 'inc':
        item.quantity += 1
    elif action == 'dec' and item.quantity > 1:
        item.quantity -= 1

    item.save()
    return redirect('cart')

def billing_info(request):
    session_id = get_session_id(request)
    items = CartItem.objects.filter(session_id=session_id)

    subtotal = sum([item.subtotal() for item in items])
    shipping = 0
    total = subtotal + shipping

    related_products = Product.objects.filter(stock__gt=0)[:4]

    return render(request, 'orders/billing_info.html', {
        'items': items,
        'subtotal': subtotal,
        'shipping': shipping,
        'total': total,
        'related_products': related_products,
    })