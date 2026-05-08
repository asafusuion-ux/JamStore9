from django.db import models


class Gallery(models.Model):
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE,related_name='images', verbose_name='Фотки')
    image = models.ImageField(upload_to='gallery/', verbose_name='Фото')

    def __str__(self):
        return f"Фото '{self.product.name}' "

    class Meta:
        verbose_name = 'Галлерея'
        verbose_name_plural = 'Галлерея'