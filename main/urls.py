from django.urls import path
from main.views import ProductListView, contacts, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView
from main.apps import MainConfig

app_name = MainConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/product/', ProductDetailView.as_view(), name='product'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
]
