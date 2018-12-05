from django.db import models

class CarouselleImage(models.Model):
    photo = models.ImageField(upload_to='')
    firstField = models.BooleanField(default=False, verbose_name='Картинка будет отображаться первой')

    class Meta:
        verbose_name = 'Картинка для карусели'
        verbose_name_plural = 'Картинки для карусели'