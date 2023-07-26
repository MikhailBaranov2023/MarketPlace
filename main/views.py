from django.shortcuts import render
from main.models import Product, Category


def home(requests):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Товары'
    }
    return render(requests, 'main/home.html', context)


# Create your views here.
def product(requests, pk):
    product_list = Product.objects.filter(id=pk)
    context = {
        'object_list': product_list,
        'title': 'Продукты'
    }
    return render(requests, 'main/product.html', context)


def contacts(requests):
    if requests.method == 'POST':
        name = requests.POST.get('name')
        email = requests.POST.get('email')
        message = requests.POST.get('massage')
        print(f'{name}({email}): {message}')

    context = {
        'title': 'Контакты'
    }

    return render(requests, 'main/contacts.html', context)
