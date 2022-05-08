from django.contrib.auth import  views as auth_view
from django.urls import path

from . import views

urlpatterns = [
    path('become-customer/', views.become_customer, name='become_customer'),
    path('your_car/', views.profile_create_view, name='your_car'),

    path('logout/', auth_view.LogoutView.as_view(), name='logout'),  # django default logout view
    path('customer_login/', auth_view.LoginView.as_view(template_name='customer/customer_login.html'), name='customer_login') # django default login
]