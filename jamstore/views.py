from django.views.generic import TemplateView
from apps.product.models import Product, Category as Product_Category
from apps.blog.models import News, Category as Blog_Category
from django.db.models import Q

class GlobalSearchView(TemplateView):
    template_name = 'search/globalsearch.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '')
        if query:
            context['products'] = Product.objects.filter(
                Q(name__icontains=query) |
                Q(sku__icontains=query) |
                Q(category__name__icontains=query)
            ).distinct()[:6]
            context['news'] = News.objects.filter(
                Q(title__icontains=query) |
                Q(category__name__icontains=query)
            ).distinct()[:6]
            context['blog_categories'] = Blog_Category.objects.filter(
                Q(name__icontains=query)
            ).distinct()[:6]
        else:
            context['products'] = []
            context['news'] = []
            context['blog_categories'] = []
        return context