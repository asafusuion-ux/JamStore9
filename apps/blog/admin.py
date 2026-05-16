from django.contrib import admin
from apps.blog.models import News, Category, Tag, Comments
from django.utils.text import Truncator


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Tag)

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'short_text', 'get_blog', 'created_at')
    list_display_links = ('id', 'author', 'short_text', 'get_blog', 'created_at')
    search_fields = ('author__username', 'blog__title', 'text')

    @admin.display(description='Текст')
    def short_text(self, obj):
        return Truncator(obj.text).words(10)
    
    @admin.display(description='Новость')
    def get_blog(self, obj):
        return Truncator(obj.blog.title).chars(20) 