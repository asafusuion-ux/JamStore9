from django.db import models
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


class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, 
        related_name='products', verbose_name="Категория"
    )
    name = models.CharField(max_length=150, verbose_name="Название товара")
    image = models.ImageField(
        upload_to="product/", verbose_name="Фото", 
        null=True, blank=True
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    stock = models.PositiveIntegerField(default=0, verbose_name="Кол-во")
    sku = models.CharField(max_length=100,unique=True, verbose_name="Артикул товара")
    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.name} {self.sku}"
    
    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'Товары'

class Slider(models.Model):
    title = models.CharField(max_length=100, verbose_name='Текст заголовка')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='slider/', verbose_name='Фото')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдеры'

class SiteSettings(models.Model):
    title = models.CharField(max_length=30, verbose_name='Название сайта')
    announcement = models.CharField(max_length=120, verbose_name='Обьявление', null=True, blank=True)
    addres = models.CharField(max_length=30, verbose_name='Адрес')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    mail = models.CharField(max_length=30, verbose_name='Почта')
    working_hours = models.CharField(max_length=30,verbose_name='Время работы')
    # Соц сети instagram, facebook, ok, vk, twitter)
    instagram = models.CharField(max_length=20, verbose_name='Инстаграм', null=True, blank=True)
    facebook = models.CharField(max_length=20, verbose_name='Фейсбук', null=True, blank=True)
    wk = models.CharField(max_length=20, verbose_name='Вк', null=True, blank=True)
    twitter = models.CharField(max_length=20, verbose_name='Твиттер', null=True, blank=True)
    # Мессенджеры
    whatsapp = models.CharField(max_length=20, verbose_name="Ватсап", null=True, blank=True)
    telegram = models.CharField(max_length=20, verbose_name="Телеграмм", null=True, blank=True)

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Настройки сайта'
    

class Comments(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, 
    related_name='shop_comments', verbose_name='комментарии'
    )
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="product_comments")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} - {self.product.name[:20]}"
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'