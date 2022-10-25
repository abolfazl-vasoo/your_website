from django.contrib import admin
from shop import models
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_filter = ['category','is_active']
    list_display = ['title', 'price', 'is_active']
    list_editable = ['price', 'is_active']


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.ProductCategory)

