from django.urls import path
from apps.product.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('cart/', CartView.as_view(), name='cart'),
    path('about/', AboutView.as_view(), name='about'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('service/', ServiceView.as_view(), name='service'),
    path('gallery/', GalleryView.as_view(), name='gallery'),
    path('404/', ErrorView.as_view(), name='404'),
    path('search/', SearchView.as_view(), name='search'),
    # single pages
    path('shop_single/<slug:slug>/', ShopSingleView.as_view(), name='shop_single'),
]