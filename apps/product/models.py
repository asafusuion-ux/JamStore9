from django.db import models


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