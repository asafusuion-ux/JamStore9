from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from apps.users.forms import RegisterForm, LoginForm
from apps.users.models import Favorite
from apps.blog.models import News
from django.contrib.auth.decorators import login_required


def register_view(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    return render(request, 'auth/register.html', {'form': form})

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Неверный логин или пароль')
    return render(request, 'auth/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def toggle_favorite_blog(request, slug):
    blog = get_object_or_404(News, slug=slug)
    obj, created = Favorite.objects.get_or_create(
        user=request.user,
        blog=blog
    )
    if not created:
        obj.delete()
    return redirect('blog_single', slug=slug)

@login_required
def favorite_list(request):
    favorites = Favorite.objects.filter(user=request.user)\
        .select_related('blog').order_by('-created_at')
    return render(request, 'pages/favorites.html', {'favorites':favorites})

@login_required
def profile_view(request):
    favorites = Favorite.objects.filter(user=request.user)\
        .select_related('blog').order_by('-created_at')
    comments = request.user.blog_comments.select_related('blog').order_by('-created_at')
    return render(request, 'auth/profile.html', {
        'favorites': favorites,
        'comments': comments,
        'favorites_count': favorites.count(),
        'comments_count': comments.count(),
    })
