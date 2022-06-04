from django.contrib.auth import  views as auth_view
from django.urls import path

from . import views

urlpatterns = [
    path('edit-product/<int:pk>/', views.edit_product, name='edit_product'),
    path('become-vendor/', views.become_vendor, name='become_vendor'),
    path('vendor-admin/', views.vendor_admin, name='vendor_admin'),
    path('add-product/', views.add_product, name='add_product'),
    path('edit-vendor/', views.edit_vendor, name='edit_vendor'),

    path('your_location/', views.vendor_profile, name='your_location'),

    path('logout/', auth_view.LogoutView.as_view(), name='logout'), #django default logout view
    path('login/', auth_view.LoginView.as_view(template_name='vendor/login.html'), name='login'),  # django default login

    path('',views.vendors, name = 'vendors'),
    path('<int:vendor_id>/',views.vendor, name = 'vendor'),

    path('delete_item/<item_id>', views.delete_item, name='delete-item'),
]