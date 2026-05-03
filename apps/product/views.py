from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from apps.product.models import *
from django.db.models import Count, Prefetch

class HomeView(TemplateView):
    template_name = 'index.html'
     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all().order_by('-id')[:8]
        context['products'] = Product.objects.all().order_by('-id')[:6]
        context['sliders'] = Slider.objects.all().order_by('-id')[:3]
        return context

# category start
class ShopView(TemplateView):
    template_name = 'pages/shop.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        categories = Category.objects.annotate(
            products_count=Count('products')
        ).filter(products_count__gt=0).prefetch_related(
            Prefetch(
                'products',
                queryset=Product.objects.all(),
                to_attr='all_products'
            )
        )
        context['categories'] = categories
        return context
# category end

# PAGES START
class ContactView(TemplateView):
    template_name = 'pages/contact.html'

class AboutView(TemplateView):
    template_name = 'pages/about.html'
    
class CheckoutView(TemplateView):
    template_name = 'pages/checkout.html'

class ServiceView(TemplateView):
    template_name = 'pages/service.html'

class BlogView(TemplateView):
    template_name = 'pages/blog.html'

class CartView(TemplateView):
    template_name = 'pages/cart.html'

class GalleryView(TemplateView):
    template_name = 'pages/gallery.html'

class ErrorView(TemplateView):
    template_name = 'pages/404.html'

class ShopSingleView(TemplateView):
    template_name = 'single_pages/shop_single.html'
# PAGES END