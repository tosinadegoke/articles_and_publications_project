from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.

from .forms import ArticleForm
from .models import Article, Post

from django.views.generic import (TemplateView, ListView,
                                DetailView, UpdateView,
                                CreateView, DeleteView)

# template files is stored in templates folder under the app folder or on the root templates (after settings.py have been updated)
# ArticleListView template name is article_list.html - context =object_list 
# ArticleDetailView template name is article_detail.html - context =object
# ArticleCreateView and ArticleUpdateView template_name is article_form.html - context = form
# ArticleDeleteView template name is article_confirm_delete.html - context=object

class ArticleListView(ListView):
    # queryset=Article.objects.all()
    queryset=Article.objects.order_by('-pk')
    #context_object_name='Articles'
    # model= Article
    #template_name='article_list.html'
    #paginate_by=10

class ArticleDetailView(DetailView):
    model=Article   #   the url path must be the 'pk' of the object
    # template_name='article_detail.html'

    # if this function is introduced, the url path '<int:pk>/details/' must be changed to '<int:id>/details/'
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id = id_)

class ArticleCreateView(CreateView):
    model = Article
    # fields=('__all__')
    form_class = ArticleForm

    def form_valid(self, form):
        print(form.cleaned_data)    # prints the data entered as dictionary in the terminal
        return super().form_valid(form)

    # to override the default url(get_absolute_url), you redirect to a specific url as below
    # def get_success_url(self):
    #     return '/Blog/'

class ArticleUpdateView(UpdateView):
    model = Article
    fields=('__all__')
    # form_class = ArticleForm
    # template_name='article_form.html'

class ArticleDeleteView(DeleteView):
    model = Article
    # template_name = 'article_confirm_delete.html'
    # success_url = reverse_lazy('article_list')

    def get_success_url(self) -> str:
        return super().get_success_url()


####    CLASS BASED VIEWS FOR POST MODELS   ####

# template files is stored in templates folder under the app folder or on the root templates (after settings.py have been updated)
# PostListView template name is post_list.html - context =object_list 
# PostDetailView template name is post_detail.html - context =object
# PostCreateView and PostUpdateView template_name is post_form.html - context = form
# PostDeleteView template name is post_confirm_delete.html - context=object

class PostListView(ListView):
    # queryset=Post.objects.order_by('-pk')      # change the order from starting last to first or use - # ordering = ['-date_posted']
    ordering = ['-date_posted']
    #context_object_name='posts'
    model= Post
    #template_name='post_list.html'
    paginate_by = 4                         # it sets the number of items on each page


class UserPostListView(ListView):
    """Class to display Posts by a specific user or author
    """    
    # queryset=Post.objects.order_by('-pk')      # change the order from starting last to first or use - # ordering = ['-date_posted']
    #context_object_name='posts'
    model= Post
    template_name='Blog/user_post.html'
    paginate_by = 4                         # it sets the number of items on each page

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))  # Get the user
        return Post.objects.filter(author=user).order_by('-date_posted')         # Filter the Posts to the ones by the author


class PostDetailView(DetailView):
    model=Post
    # template_name='post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields=('title', 'content')     # Though author required, we will make the signed user the author the post by overriding the form_valid() method

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    # messages.success(f'Your account has been updated!')
    # success_url=reverse_lazy('post_list') or we can define a get_absolute_url in the model.py for redirecting django


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields=('title', 'content')
    # success_url=reverse_lazy('post_list')     -   used get_absolute_url() instead
    # template_name='post_form.html'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()    # this gets the current post
        if self.request.user == post.author:    # check if the current login user is the same as the author of the post
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    
    def test_func(self):
        post = self.get_object()    # this gets the current post
        if self.request.user == post.author:    # check if the current login user is the same as the author of the post
            return True
        return False
    
    success_url=reverse_lazy('post_list')
