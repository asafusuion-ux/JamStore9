from django.contrib import admin
from apps.product.models import Slider, Category, Product, SiteSettings, Gallery


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku')
    list_display_links = ('name', 'sku')
    prepopulated_fields = {'slug':('name',)}
    search_fields = ('name', 'sku')

admin.site.register(Slider)

admin.site.register(SiteSettings)

admin.site.register(Gallery)