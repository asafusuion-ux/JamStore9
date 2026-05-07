from django.views.generic import TemplateView, ListView, DetailView
from apps.blog.models import News

class BLogView(ListView):
    model = News
    template_name = 'pages/blog.html'
    context_object_name = 'blog'


class AboutView(TemplateView):
    template_name = 'pages/about.html'

class BlogSingleView(DetailView):
    model  = News
    template_name = 'single_pages/blog_single.html'
    slug_field = 'slug'
    context_object_name = 'blog'