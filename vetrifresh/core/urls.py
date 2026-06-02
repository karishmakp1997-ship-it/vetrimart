from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('check-pincode/', views.check_pincode, name='check_pincode'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact_view, name='contact'),
]