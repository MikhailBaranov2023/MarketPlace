# Generated by Django 4.2.3 on 2023-08-10 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование категории')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание категории')),
            ],
            options={
                'verbose_name': 'Категориsя',
                'verbose_name_plural': 'Категории',
                'ordering': ('name', 'description'),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название товара')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='Превью')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('make_date', models.DateField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('change_date', models.DateField(auto_now_add=True, null=True, verbose_name='Дата последнего изменения')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'продукты',
                'ordering': ('name', 'category', 'description'),
            },
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_number', models.IntegerField(verbose_name='номер версии')),
                ('version_name', models.CharField(max_length=150, verbose_name='название версии')),
                ('is_active', models.BooleanField(default=True, verbose_name='активная версяи')),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product', verbose_name='название товара')),
            ],
            options={
                'verbose_name': 'версия',
                'verbose_name_plural': 'версии',
            },
        ),
    ]
