from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    header = models.CharField(max_length=100, verbose_name='Загаловок')
    body = models.TextField(verbose_name='Содержимое')
    image = models.ImageField(verbose_name='Превью', **NULLABLE)
    create_date = models.DateField(verbose_name='Дата создания', **NULLABLE)

    is_published = models.BooleanField(default=True, verbose_name='Признак публикации')
    view_count = models.IntegerField(default=0, verbose_name='просмотры')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
