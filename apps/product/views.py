from django.views.generic import TemplateView, DetailView, ListView
from django.shortcuts import get_object_or_404, redirect
from apps.product.models import *
from django.db.models import Count, Prefetch
from apps.blog.models import News


class HomeView(TemplateView):
    template_name = 'index.html'
     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all().order_by('-id')[:8]
        context['products'] = Product.objects.all().order_by('-id')[:6]
        context['sliders'] = Slider.objects.all().order_by('-id')[:3]
        context['news'] = News.objects.all().order_by('-id')[:6]
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
class AboutView(TemplateView):
    template_name = 'pages/about.html'
    
class CheckoutView(TemplateView):
    template_name = 'pages/checkout.html'

class ServiceView(TemplateView):
    template_name = 'pages/service.html'


class CartView(TemplateView):
    template_name = 'pages/cart.html'
    
class ErrorView(TemplateView):
    template_name = 'pages/404.html'

class ShopSingleView(DetailView):
    model  = Product
    template_name = 'single_pages/shop_single.html'
    slug_field = 'slug'
    context_object_name = 'product'

    queryset = Product.objects.select_related('category')
# PAGES END

def add_shop_comment(request, product_slug):
    if request.method == "POST" and request.user.is_authenticated:
        product_item = get_object_or_404(Product, slug=product_slug)
        text = request.POST.get('text')
        
        if text:
            Comments.objects.create(
                product=product_item,
                author=request.user,
                text=text
            )
    return redirect(request.META.get('HTTP_REFERER', '/'))