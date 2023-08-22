from django.urls import path
from main.views import ProductListView, contacts, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView
from main.apps import MainConfig
from django.views.decorators.cache import cache_page, never_cache

app_name = MainConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/product/', cache_page(60)(ProductDetailView.as_view()), name='product'),
    path('create/', never_cache(ProductCreateView.as_view()), name='create'),
    path('edit/<int:pk>/', never_cache(ProductUpdateView.as_view()), name='edit'),
    path('delete/<int:pk>/', never_cache(ProductDeleteView.as_view()), name='delete'),
]
