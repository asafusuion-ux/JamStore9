from django.urls import path 
from apps.gallery.views import GalleryView


urlpatterns = [
    path('', GalleryView.as_view(), name='gallery'),
]
