from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    fields = ('name', 'price', 'category')

admin.site.register(Product, ProductAdmin)