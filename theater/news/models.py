from django.db import models

class Post (models.Model):
    name = models.TextField(max_length=200, verbose_name='Заголовок', primary_key=True)
    photo = models.ImageField(upload_to='')
    text = models.TextField(max_length=3000, verbose_name='Текст новости')
    #creationDate = models.DateTimeField.auto_now_add

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'