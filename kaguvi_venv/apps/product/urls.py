from django.urls import path

from . import  views

urlpatterns = [
    path('search/', views.search, name = 'search'),
    path('<slug:category_slug>/<slug:product_slug>/<int:product_id>/', views.product, name = 'product'),
    path('<slug:category_slug>/', views.category, name='category'),
]