from django.contrib import admin
from .models import Product, Status

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'price', 'date', 'status')
    search_fields = ('name', 'price')

class StatusAdmin(admin.ModelAdmin):
    list_display = ('numero', 'libelle')
    search_fields = ('libelle',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Status, StatusAdmin)