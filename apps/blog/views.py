from django.views.generic import TemplateView, ListView, DetailView
from apps.blog.models import News, Comments
from django.db.models import Count
from django.shortcuts import redirect, get_object_or_404

class BLogView(ListView):
    model = News
    template_name = 'pages/blog.html'
    context_object_name = 'blog'
    paginate_by = 6

    def get_queryset(self):
        return News.objects.annotate(comments_count=Count('comments'))

class AboutView(TemplateView):
    template_name = 'pages/about.html'

class BlogSingleView(DetailView):
    model = News
    template_name = 'single_pages/blog_single.html'
    slug_field = 'slug'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_blogs'] = News.objects.order_by('-id')[:3]
        return context

def add_comment(request, news_slug): # Теперь принимаем news_slug
    if request.method == "POST" and request.user.is_authenticated:
        # Ищем новость по слагу
        news_item = get_object_or_404(News, slug=news_slug)
        text = request.POST.get('text')
        
        if text:
            Comments.objects.create(
                blog=news_item,
                author=request.user,
                text=text
            )
    return redirect(request.META.get('HTTP_REFERER', '/'))