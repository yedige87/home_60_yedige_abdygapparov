from django.contrib import admin

from shop_app.models.products import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text')
    list_filter = ('id', 'title', 'text')
    search_fields = ('title', 'text')
    fields = ('text', 'title')
   # readonly_fields = ('id', 'created_at', 'updated_at', 'created_at')

admin.site.register(Product, ProductAdmin)
