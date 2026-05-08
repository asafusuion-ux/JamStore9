from django.views.generic import ListView
from apps.gallery.models import Gallery

class GalleryView(ListView):
    model = Gallery
    template_name = 'pages/gallery.html'
    context_object_name = 'photos'
    paginate_by = 5
     

    def get_queryset(self):
        return Gallery.objects.order_by('-id')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['gallery'] = Gallery.objects.all()
    #     return context