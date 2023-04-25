from django.contrib import admin
from .models import Product, Variation

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_descripition', 'get_formated_amount', 'slug', 'promotional_amount',]


@admin.register(Variation)
class VariationtAdmin(admin.ModelAdmin):
    list_display = ['name', 'product', 'amount', 'stock', 'promotional_amount',]
