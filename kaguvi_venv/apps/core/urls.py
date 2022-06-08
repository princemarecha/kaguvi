from django.urls import path # touse path when adding urls
from . import  views #import views in the current folder

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('contact/', views.contact , name='contact'),
    path('delete_car/<car_id>', views.delete_car, name='delete-car'),
]
