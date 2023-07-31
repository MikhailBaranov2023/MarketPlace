from django.shortcuts import render
from main.models import Product, Category
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/product_detail.html'


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'image', 'category', 'price',)
    success_url = reverse_lazy('main:home')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'description', 'image', 'category', 'price',)
    success_url = reverse_lazy('main:home')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('main:home')


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
