from django.contrib import admin

from product.models import Product, ProductCategory, Basket

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity','category')
    fields = ('name', 'price', 'quantity', 'category', 'description', 'image')
    search_fields = ('name', 'price', 'quantity', 'category')
    ordering = ('name',)

class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0
