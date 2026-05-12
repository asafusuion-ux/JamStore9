from django.urls import path
from apps.blog.views import BLogView, AboutView, BlogSingleView, add_comment, BLogSearchView


urlpatterns = [
    path('', BLogView.as_view(), name='blog'),
    path('search/', BLogSearchView.as_view(), name='blog_search'),
    path('about/', AboutView.as_view(), name='about'),
    path('blog_single/<slug:slug>/', BlogSingleView.as_view(), name='blog_single'),
    path('add_comment/<slug:news_slug>/', add_comment, name='add_comment'),
]
