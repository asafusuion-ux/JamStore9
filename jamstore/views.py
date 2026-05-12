from django.views.generic import TemplateView
from apps.product.models import Product, Category
from apps.blog.models import News

class GlobalSearchView(TemplateView):
    template_name = 'search/globalsearch.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '')
        if query:
            context['products'] = Product.objects.filter(name__icontains=query)[:6]
            context['categories'] = Category.objects.filter(name__icontains=query)[:6]
            context['news'] = News.objects.filter(title__icontains=query)[:6]
        else:
            context['products'] = []
            context['categories'] = []
            context['news'] = []
        return context