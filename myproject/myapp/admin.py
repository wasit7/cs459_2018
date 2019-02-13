from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    fields = ('name', 'price', 'category', 'image')
    list_display = ('name', 'price', 'category', 'image')
    list_filter = ('category', 'price', )
    list_editable = ('price', 'category', 'image', )

admin.site.register(Product, ProductAdmin)