from django.contrib import admin

# Register your models here.
from .models import Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','offer','created_at')
    search_fields = ('name','offer')
    list_filter = ('created_at',)
    ordering = ('-created_at',)