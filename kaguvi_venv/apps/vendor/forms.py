#this will make it possible for vendor to add products
from django.forms import ModelForm
from  django import forms

from apps.product.models import  Product
from apps.vendor.models import vendorProfile

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'image', 'title', 'description', 'price', 'car', 'model', 'engine']

class vendorProfile(forms.ModelForm):
    class Meta:
        model = vendorProfile
        fields = ['vendor','address','latitude','longitude','color', 'title', 'subTitle']
        labels = {"vendor":""}
        widgets ={
            'address': forms.TextInput(attrs={'placeholder': '00 Kaguvi Street, Hre'}),
            'color': forms.TextInput(attrs={'placeholder': 'blue'}),
            'latitude': forms.TextInput(attrs={'placeholder': '-17.123456'}),
            'longitude': forms.TextInput(attrs={'placeholder': '34.46364636'}),
            'title': forms.TextInput(attrs={'placeholder': 'Mr Vendor'}),
            'subTitle': forms.TextInput(attrs={'placeholder': 'Auto Parts Sale'}),
        }

