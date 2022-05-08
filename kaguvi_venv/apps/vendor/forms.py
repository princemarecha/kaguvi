#this will make it possible for vendor to add products
from django.forms import ModelForm

from apps.product.models import  Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'image', 'title', 'description', 'price', 'car', 'model', 'engine']
