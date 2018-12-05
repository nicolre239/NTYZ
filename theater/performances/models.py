from django.db import models

class Scene (models.Model):
    sceneType = models.TextField(max_length=32, verbose_name='Тип сцены', unique=True, primary_key=True)

    def __str__(self):
        return "%s" % self.sceneType

    class Meta:
        verbose_name = 'Сцена'
        verbose_name_plural = 'Сцены'

class PerfType (models.Model):
    perfType = models.TextField(max_length=32, verbose_name='Тип спектакля', unique=True, primary_key=True)

    def __str__(self):
        return "%s" % self.perfType

    class Meta:
        verbose_name = 'Тип спектакля'
        verbose_name_plural = 'Типы спектаклей'


class Performance (models.Model):
    name = models.TextField(max_length=100, verbose_name='Название спектакля', primary_key=True)
    photo = models.ImageField(upload_to='')
    dateTime = models.DateTimeField(verbose_name='Дата и время')
    scene = models.ForeignKey(Scene, on_delete=None, verbose_name='Сцена')
    perfType = models.ForeignKey(PerfType, on_delete=None, verbose_name='Тип спектакля')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Спектакль'
        verbose_name_plural = 'Спектакли'