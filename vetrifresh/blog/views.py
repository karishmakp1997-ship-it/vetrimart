from django.shortcuts import render
from .models import BlogPost

def blog_list(request):
    posts = BlogPost.objects.filter(is_active=True).order_by('-published_at')

    selected_category = request.GET.get('category')
    selected_tag = request.GET.get('tag')
    selected_price = request.GET.get('price', '')
    sort = request.GET.get('sort', 'latest')

    if selected_category:
        posts = posts.filter(category__iexact=selected_category)

    if sort == 'oldest':
        posts = posts.order_by('published_at')
        
    elif sort == 'title':
        posts = posts.order_by('title')
    else:
        posts = posts.order_by('-published_at')

    categories = BlogPost.objects.filter(is_active=True).values_list('category', flat=True).distinct().order_by('category')
    tags = ["Healthy", "Low fat", "Vegetarian", "Kid foods", "Vitamins", "Bread", "Meat", "Snacks", "Tiffin", "Lunch", "Dinner", "Breakfast", "Fruit"]

    recent_posts = BlogPost.objects.filter(is_active=True).order_by('-published_at')[:3]
    sale_posts = BlogPost.objects.filter(is_active=True).order_by('-published_at')[:3]
    gallery_posts = BlogPost.objects.filter(is_active=True).order_by('-published_at')[:8]

    return render(request, 'blog/blog_list.html', {
        'posts': posts,
        'categories': categories,
        'tags': tags,
        'recent_posts': recent_posts,
        'sale_posts': sale_posts,
        'gallery_posts': gallery_posts,
        'selected_category': selected_category,
        'selected_tag': selected_tag,
        'selected_price': selected_price,
        'sort': sort,
        'hide_chatbot': True,
    })