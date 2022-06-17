from django.urls import path
from .views import (
            book_create_view, 
            book_edit_view,
            book_list_view,
            book_delete_view,
            book_detail_view
        )
        
urlpatterns = [
    path('', book_list_view, name= 'list_book'),
    path('create', book_create_view, name= 'create_book'),
    path('<int:book_id>/update', book_edit_view, name= 'edit_book'),
    path('<int:book_id>/details', book_detail_view, name= 'detail_book'),
    path('<int:book_id>/delete', book_delete_view, name= 'delete_book'),
]
