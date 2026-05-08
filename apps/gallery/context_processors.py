from apps.gallery.models import Gallery

def gallery_footer(request):
    return{
        'footer_gallery': Gallery.objects.order_by('-id')[:6]
    }