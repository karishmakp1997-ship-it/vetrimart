from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'pincode', 'total', 'status', 'created_at']
    list_editable = ['status']
    list_filter = ['status']
    inlines = [OrderItemInline]