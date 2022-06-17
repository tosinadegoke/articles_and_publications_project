from django.urls import path

from .views import (
            PostListView, PostDetailView,
            PostCreateView, PostUpdateView,
            PostDeleteView, UserPostListView,

            ArticleCreateView, ArticleDeleteView,
            ArticleDetailView, ArticleListView,
            ArticleUpdateView,
            )

from .views_func_based import (
            article_home_view as ahv,
            article_create_view as acv, 
            article_detail_view as adv,
            article_list_view as alv,
            article_about_view as abv,
            )       

urlpatterns = [
    path('', PostListView.as_view(), name="post_list"),
    path('user/<str:username>', PostListView.as_view(), name="user_posts"),
    path('<int:pk>/details/', PostDetailView.as_view(), name= "post_detail"),
    path('create/', PostCreateView.as_view(), name= "post_create"),
    path('<int:pk>/update/', PostUpdateView.as_view(), name= "post_update"),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name= "post_delete"),
    path('about/', abv, name = 'article_about')

#     path('', ArticleListView.as_view(), name="article_list"),
#     path('<int:id>/details/', ArticleDetailView.as_view(), name= "article_detail"),
#     path('create', ArticleCreateView.as_view(), name= "article_create"),
#     path('<int:pk>/update/', ArticleUpdateView.as_view(), name= "article_update"),
#     path('<int:pk>/delete/', ArticleDeleteView.as_view(), name= "article_delete"),

]




                    

# urlpatterns = [
#     # path('', ahv, name = 'article_home'),
#     path('about/', abv, name = 'article_about'),
    
#     path('create', acv, name= "article_create"),
#     path('<int:article_id>/details/', adv, name= "article_detail"),
#     path('list', alv, name="article_list")
# ]

