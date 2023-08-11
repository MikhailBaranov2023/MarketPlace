from django.db import models
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование категории')
    description = models.TextField(**NULLABLE, verbose_name='Описание категории')

    # created_at = models.DateField(verbose_name='Дата добавления', default=datetime.date.today())

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категориsя'
        verbose_name_plural = 'Категории'
        ordering = ('name', 'description',)


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название товара')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    image = models.ImageField(upload_to='product/', verbose_name='Превью', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.IntegerField(verbose_name='Цена')
    make_date = models.DateField(verbose_name='Дата создания', auto_now_add=True, **NULLABLE)
    change_date = models.DateField(verbose_name='Дата последнего изменения', auto_now_add=True, **NULLABLE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name', 'category', 'description',)


class Version(models.Model):
    product_name = models.ForeignKey(Product, verbose_name='название товара', on_delete=models.CASCADE)
    version_number = models.IntegerField(verbose_name='номер версии')
    version_name = models.CharField(max_length=150, verbose_name='название версии')
    is_active = models.BooleanField(default=True, verbose_name='активная версяи')

    def __str__(self):
        return self.version_name

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
