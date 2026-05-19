from django.urls import path 
from apps.users.views import  *

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('favorites/blog/<slug:slug>/', toggle_favorite_blog, name='toggle_favorite_blog'),
    path('favorite_list/', favorite_list, name='favorite_list'),
    path('profile/', profile_view, name='profile'),
]
