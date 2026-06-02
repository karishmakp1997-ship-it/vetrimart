from django.db import models

class ServiceablePincode(models.Model):
    pincode = models.CharField(max_length=6, unique=True)
    area_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.pincode} - {self.area_name}"

    class Meta:
        verbose_name = "Serviceable Pincode"

class Banner(models.Model):
    BANNER_TYPE = (
        ('main', 'Main Hero Banner'),
        ('side', 'Side Banner'),
        ('flash', 'Flash Sale Banner'),
    )
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)
    offer_text = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='banners/')
    button_text = models.CharField(max_length=50, default='Shop Now')
    button_link = models.CharField(max_length=200, default='/')
    banner_type = models.CharField(max_length=20, choices=BANNER_TYPE)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class DealBanner(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)
    price_text = models.CharField(max_length=100, blank=True)
    discount_text = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='banners/deals/')
    bg_color = models.CharField(max_length=20, default='#1a3c1a')
    has_countdown = models.BooleanField(default=False)
    countdown_end = models.DateTimeField(null=True, blank=True)
    button_link = models.CharField(max_length=200, default='/')
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, default='Customer')
    review = models.TextField()
    photo = models.ImageField(upload_to='testimonials/', blank=True)
    rating = models.IntegerField(default=5)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class InstagramPhoto(models.Model):
    image = models.ImageField(upload_to='instagram/')
    link = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"Instagram Photo {self.id}"

class FeatureBanner(models.Model):
    LOGO_POSITION = (
        ('left', 'Left'),
        ('center', 'Center'),
        ('right', 'Right'),
    )
    image = models.ImageField(upload_to='banners/feature/')
    title = models.CharField(max_length=200, blank=True)
    subtitle = models.CharField(max_length=200, blank=True)
    button_text = models.CharField(max_length=50, default='Shop Now')
    button_link = models.CharField(max_length=200, default='/')
    logo_position = models.CharField(max_length=10, choices=LOGO_POSITION, default='left')
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"Feature Banner - {self.logo_position} - {self.order}"

    class Meta:
        ordering = ['order']