from django import forms

from .models import Customer

class CustomerProfile(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'user',
            'name',
            'car',
            'model',
            'engine'
        ]
        labels = {"user": ""}
        widgets = {
            # 'address': forms.TextInput(attrs={'class': 'form-control'}),
            # 'color': forms.TextInput(attrs={'class': 'form-control'}),
        }