from django.urls import path
from blog.views import BlogListView, BlogCreateView, BlogUpdateView, BlogDeleteView, BlogDetailView
from blog.apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='list'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('edit/<slug:slug>/', BlogUpdateView.as_view(), name='edit'),
    path('delete/<slug:slug>/', BlogDeleteView.as_view(), name='delete'),
    path('view/<slug:slug>/', BlogDetailView.as_view(), name='view'),
]
