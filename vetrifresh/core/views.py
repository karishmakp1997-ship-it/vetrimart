from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

from .models import (
    Banner,
    DealBanner,
    Testimonial,
    InstagramPhoto,
    ServiceablePincode,
    FeatureBanner,
)
from products.models import Category, Product
from blog.models import BlogPost


def home(request):
    main_banners = Banner.objects.filter(banner_type='main', is_active=True).order_by('order')
    side_banners = Banner.objects.filter(banner_type='side', is_active=True).order_by('order')
    flash_banner = Banner.objects.filter(banner_type='flash', is_active=True).first()
    deal_banners = DealBanner.objects.filter(is_active=True).order_by('order')
    categories = Category.objects.filter(is_active=True).order_by('order')
    popular_products = Product.objects.filter(is_popular=True, is_active=True)[:8]
    latest_blogs = BlogPost.objects.filter(is_active=True).order_by('-published_at')[:3]
    testimonials = Testimonial.objects.filter(is_active=True)
    instagram_photos = InstagramPhoto.objects.filter(is_active=True).order_by('order')[:6]
    nav_categories = Category.objects.filter(is_active=True).order_by('order')[:7]
    feature_banners = FeatureBanner.objects.filter(is_active=True).order_by('order')

    context = {
        'main_banners': main_banners,
        'side_banners': side_banners,
        'flash_banner': flash_banner,
        'deal_banners': deal_banners,
        'categories': categories,
        'popular_products': popular_products,
        'latest_blogs': latest_blogs,
        'testimonials': testimonials,
        'instagram_photos': instagram_photos,
        'nav_categories': nav_categories,
        'feature_banners': feature_banners,
    }
    return render(request, 'core/home.html', context)


def check_pincode(request):
    pincode = request.GET.get('pincode', '')
    try:
        pin = ServiceablePincode.objects.get(pincode=pincode, is_active=True)
        return JsonResponse({'available': True, 'area': pin.area_name})
    except ServiceablePincode.DoesNotExist:
        return JsonResponse({'available': False})


def about(request):
    return render(request, 'core/about.html')


def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message_text = request.POST.get("message")

        # TODO: save to model or send_mail

        messages.success(request, "Your message has been sent successfully!")
        return redirect('contact')

    return render(request, 'core/contact.html')