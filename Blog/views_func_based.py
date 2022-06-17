from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render
from django.template import context

# Create your views here.

from .forms import ArticleForm
from .models import Article, Post



def article_home_view(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, 'Blog/index.html', context)

def article_about_view(request):
    return render(request, 'Blog/about.html', {})

def article_create_view(request):
    my_form = ArticleForm(request.POST or None)
    if my_form.is_valid():
        my_form.save()
        my_form = ArticleForm()
    
    context = {
        'form' : my_form
    }

    return render(request, 'Blog/article_create.html', context)

def article_detail_view(request, article_id):
    obj = get_object_or_404(Article, id = article_id)
    context = {
        'article_obj' : obj
    }

    return render(request, 'Blog/article_details.html', context)
# def book_detail_view(request, book_id):
#     obj = get_object_or_404(Book, id = book_id)

#     context = {
#         'book_object' : obj
#     }
#     return render(request, 'bookstore/book_detail.html', context)

def article_list_view(request):
    obj = Article.objects.all()

    context = {
        'article_list' : obj
    }
    return render(request, 'Blog/article_list.html', context)