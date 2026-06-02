from django.contrib import admin
from .models import ServiceablePincode, Banner, DealBanner, Testimonial, InstagramPhoto, FeatureBanner

@admin.register(ServiceablePincode)
class PincodeAdmin(admin.ModelAdmin):
    list_display = ['pincode', 'area_name', 'is_active']
    list_editable = ['is_active']

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'banner_type', 'is_active', 'order']
    list_editable = ['is_active', 'order']
    list_filter = ['banner_type']

@admin.register(DealBanner)
class DealBannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'has_countdown', 'is_active', 'order']
    list_editable = ['is_active', 'order']

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'rating', 'is_active']
    list_editable = ['is_active']

@admin.register(InstagramPhoto)
class InstagramPhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'link', 'is_active', 'order']
    list_editable = ['is_active', 'order']

@admin.register(FeatureBanner)
class FeatureBannerAdmin(admin.ModelAdmin):
    list_display = ['id', 'logo_position', 'title', 'is_active', 'order']
    list_editable = ['is_active', 'order', 'logo_position']

