from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart_page, name='cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update/<int:product_id>/<str:action>/', views.update_quantity, name='update_quantity'),
    path('billing-info/', views.billing_info, name='billing_info'),
]