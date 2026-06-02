from django.contrib import admin
from django.utils.html import format_html
from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'is_active', 'published_at', 'image_preview')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('category', 'is_active', 'published_at')
    search_fields = ('title', 'category', 'author', 'content')
    readonly_fields = ('image_preview',)

    fieldsets = (
        ('Blog Info', {
            'fields': ('title', 'slug', 'image', 'image_preview', 'category', 'content')
        }),
        ('Meta Info', {
            'fields': ('author', 'comments_count', 'is_active')
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="90" style="border-radius:6px;" />', obj.image.url)
        return "No Image"

    image_preview.short_description = 'Preview'