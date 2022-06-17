from django.shortcuts import get_object_or_404, redirect, render

from .forms import BookForm, RawBookForm
from .models import Book

# Create your views here.


def book_create_view(request):
    my_form = RawBookForm(request.POST or None)
    if my_form.is_valid():
        print(my_form.cleaned_data)
        Book.objects.create(**my_form.cleaned_data)
        my_form = RawBookForm()
    context = {
        'form' : my_form,
    }

    return render(request, 'bookstore/create_book.html', context)

def book_edit_view(request, book_id):
    obj = get_object_or_404(Book, id = book_id)
    my_form = BookForm(request.POST or None, instance = obj)
    if my_form.is_valid():  #   validates the form and generate cleaned_data
        my_form.save()

        return redirect('list_book')
        # my_form = BookForm()
    context = {
        'form' : my_form
    }
    return render(request, 'bookstore/book_create.html', context)
    

def book_list_view(request):
    my_books = Book.objects.all()
    context = {
        'book_list' : my_books
    }

    return render(request, 'bookstore/list_book.html', context)

def book_detail_view(request, book_id):
    obj = get_object_or_404(Book, id = book_id)

    context = {
        'book_object' : obj
    }
    return render(request, 'bookstore/book_detail.html', context)

def book_delete_view(request, book_id):
    obj = get_object_or_404(Book, id = book_id)
    if request.method == 'POST':
        obj.delete()
        return redirect('list_book')
    
    context = {
        'object' : obj
    }
    return render(request,  'bookstore/book_delete.html', context)

# def book_create_view(request):
#     my_form = BookForm(request.POST or None)
#     if my_form.is_valid():
#         print(my_form.cleaned_data)
#         my_form.save()
#         my_form = BookForm()
#     context = {
#         'form' : my_form,
#     }

#     return render(request, 'bookstore/create_book.html', context)

