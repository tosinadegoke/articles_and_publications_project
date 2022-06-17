from django import forms
from django.forms.widgets import TextInput, Textarea

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description', 
            'price'
        ]

class RawProductForm(forms.Form):
    title = forms.CharField(label='', 
                    widget=TextInput(
                        attrs={
                            'placeholder': 'Product Title',
                            'id':           'prod_title' 
                            }))
    description = forms.CharField(
                    required=False,
                    widget=forms.Textarea(
                        attrs={
                            'placeholder':  'Product Description',
                            'id':           'prod_desc',
                            'rows':         10,
                            'cols':         40,
                            'class':        'border border-primary text-primary'
                        }
                    )
                    )
    price = forms.DecimalField(initial= 199.90)

  
    