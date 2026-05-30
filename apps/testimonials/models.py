from django.db import models

class Review(models.Model):
    full_name = models.CharField(max_length=70, verbose_name='ФИО')
    position = models.CharField(max_length=80, verbose_name='Должность')
    text = models.CharField(max_length=180 ,verbose_name='Текст (отзыв)')
    image = models.ImageField(upload_to='testimonials/' ,verbose_name="Фото", null=True, blank=True)

    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'