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

class ContactView(TemplateView):
    template_name = 'pages/contact.html'

class AboutView(TemplateView):
    template_name = 'pages/about.html'
    
class CheckoutView(TemplateView):
    template_name = 'pages/checkout.html'

class ShopView(TemplateView):
    template_name = 'pages/shop.html'

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