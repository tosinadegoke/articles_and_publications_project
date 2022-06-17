from django import forms
from django.forms.widgets import NumberInput, Textarea, TextInput

from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'subtitle',
            'author',
            'released_date',
            'price',
        ]


class RawBookForm(forms.Form):
    title = forms.CharField(
                    max_length= 100, 
                    widget= TextInput(
                        attrs={
                            'placeholder'   :  'Book Title',
                            'id'            :  'book_title',
                            'class'         :   'text-primary'
                        }
                    )
                )

    subtitle = forms.CharField(max_length= 200, 
                    required=False,
                    widget=Textarea(
                        attrs={
                            'cols'      :   '40',
                            'rows'      :   '2',
                            'placeholder':  'Subtitle of the book'
                        }
                    )
                )
        
    author = forms.CharField(
                    max_length=100, 
                    widget=TextInput(
                        attrs={
                            'placeholder'   :   "Author's name"
                        }
                    ))
        
    price = forms.DecimalField(widget=NumberInput(
                    attrs={
                        'placeholder' : 'Price'
                    }
    ))

    released_date =  forms.DateField()