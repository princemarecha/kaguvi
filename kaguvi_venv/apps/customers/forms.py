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
            'name': forms.TextInput(attrs={'placeholder': 'Work Car #1'}),
            'car': forms.TextInput(attrs={'placeholder': 'Mazda'}),
            'model': forms.TextInput(attrs={'placeholder': '323'}),
            'engine': forms.TextInput(attrs={'placeholder': '1.2 Lt'}),

        }