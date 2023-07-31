# Generated by Django 4.2.3 on 2023-07-31 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=100, verbose_name='Загаловок')),
                ('body', models.TextField(verbose_name='Содержимое')),
                ('image', models.ImageField(upload_to='', verbose_name='Превью')),
                ('create_date', models.DateField(blank=True, null=True, verbose_name='Дата создания')),
                ('is_published', models.BooleanField(default=True, verbose_name='Признак публикации')),
                ('view_count', models.IntegerField(default=0, verbose_name='просмотры')),
                ('slug', models.CharField(blank=True, max_length=150, null=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'Блог',
                'verbose_name_plural': 'Блоги',
            },
        ),
    ]
