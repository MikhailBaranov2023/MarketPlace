from django.core.management import BaseCommand
from main.models import Category
from main.models import Product
import json


class Command(BaseCommand):
    def handle(self, *args, **options):
        category_list = [
            {'pk': 1, 'name': 'Клавиатура', 'description': 'Переферия'},
            {'pk': 2, 'name': 'Мышь', 'description': 'Переферия'},
            {'pk': 3, 'name': 'Телефон', 'description': 'Мобильное устройство'},
            {'pk': 4, 'name': 'Компьютер', 'description': 'Стационарный компьютер.'},

        ]
        Category.objects.all().delete()
        Product.objects.all().delete()

        category_for_create = []
        for category_items in category_list:
            category_for_create.append(
                Category(**category_items)
            )
        Category.objects.bulk_create(category_for_create)
