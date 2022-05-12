#this will make it possible for vendor to add products
from django.forms import ModelForm

from apps.product.models import  Product
from apps.vendor.models import vendorProfile

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'image', 'title', 'description', 'price', 'car', 'model', 'engine']

class vendorProfile(ModelForm):
    class Meta:
        model = vendorProfile
        fields = ['vendor','address', 'longitude', 'latitude','color', 'title', 'subTitle']
