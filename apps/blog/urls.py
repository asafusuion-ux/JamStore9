from django.urls import path
from apps.blog.views import BLogView, AboutView, BlogSingleView, add_comment


urlpatterns = [
    path('', BLogView.as_view(), name='blog'),
    path('about/', AboutView.as_view(), name='about'),
    path('blog_single/<slug:slug>/', BlogSingleView.as_view(), name='blog_single'),
    path('add_comment/<slug:news_slug>/', add_comment, name='add_comment'),
]
