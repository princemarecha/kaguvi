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
            #'address': forms.TextInput(attrs={'class': 'form-control'}),
            #'color': forms.TextInput(attrs={'class': 'form-control'}),
        }

