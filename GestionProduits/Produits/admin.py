from django.contrib import admin
from .models import Product, ProductAttribute, ProductAttributeValue, ProductItem
class ProductItemAdmin(admin.TabularInline):
    model = ProductItem
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('name', 'code')
    inlines = [ProductItemAdmin,]

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductItem)
admin.site.register(ProductAttribute)
admin.site.register(ProductAttributeValue)