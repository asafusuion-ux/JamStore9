from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from apps.product.models import Category, Product

class HomeView(TemplateView):
    template_name = 'index.html'
     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['products'] = Product.objects.all()
        return context