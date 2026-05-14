from django.urls import path
from apps.product.views import *


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('cart/', CartView.as_view(), name='cart'),
    path('about/', AboutView.as_view(), name='about'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('service/', ServiceView.as_view(), name='service'),
    path('404/', ErrorView.as_view(), name='404'),
    path('add_shop_comment/<slug:product_slug>/', add_shop_comment, name='add_shop_comment'),
    
    # single pages
    path('shop_single/<slug:slug>/', ShopSingleView.as_view(), name='shop_single'),
]