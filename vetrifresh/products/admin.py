from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'order']
    list_editable = ['is_active', 'order']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'badge', 'is_popular', 'is_active', 'stock']
    list_editable = ['price', 'badge', 'is_popular', 'is_active', 'stock']
    list_filter = ['category', 'badge', 'is_popular']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}