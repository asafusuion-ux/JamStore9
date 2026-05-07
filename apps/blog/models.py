from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название категории")
    image = models.ImageField(
        upload_to="category/", verbose_name="Фото",
        blank=True, null=True
    )
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

class Tag(models.Model):
    title = models.CharField(max_length=50)

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    image = models.ImageField(upload_to='news/')
    desc = CKEditor5Field('Описание', config_name='extends')
    data = models.DateTimeField(auto_now_add=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, 
        related_name='news', verbose_name="Категория", null=True
    )
    slug = models.SlugField(unique=True, blank=True)
    tag = models.ManyToManyField(Tag, blank=True)


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='новость'
        verbose_name_plural='Новости'


class Comments(models.Model):
    blog = models.ForeignKey(News, on_delete=models.CASCADE, 
    related_name='comment', verbose_name='комментарии'
    )
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)