from django.contrib import admin
from apps.product.models import Slider, Category, Product, SiteSettings, Comments
from django.utils.text import Truncator

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku')
    list_display_links = ('name', 'sku')
    prepopulated_fields = {'slug':('name',)}
    search_fields = ('name', 'sku')

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'short_text', 'product', 'created_at')
    list_display_links = ('id', 'author', 'short_text', 'product', 'created_at')
    search_fields = ('author__username', 'product__name', 'text')

    @admin.display(description='Текст')
    def short_text(self, obj):
        return Truncator(obj.text).words(10)

admin.site.register(Slider)

admin.site.register(SiteSettings)