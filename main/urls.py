from django.urls import path
from main.views import home, contacts, product
from main.apps import MainConfig

app_name = MainConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/product/', product, name='product')
]
