from django.contrib import admin

# Register your models here.
from .models import Offer

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('title','discount','active')
    search_fields = ('title',)
    list_filter = ('active',)
