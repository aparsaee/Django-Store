from django.contrib import admin
from .models import Brand, Mobile, Sold


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'slug')


@admin.register(Mobile)
class MobileAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'operating_system',
                    'screen_technology', 'screen_size', 'repository', 'status', 'slug')
    list_filter = ('brand', 'operating_system', 'screen_size')


@admin.register(Sold)
class SoldAdmin(admin.ModelAdmin):
    list_display = ('customer', 'product', 'brand', 'amount', 'date',
                    'address', 'phone', 'zip_code')
