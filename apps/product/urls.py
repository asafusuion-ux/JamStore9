from django.urls import path
from apps.product.views import HomeView, TemplateView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]