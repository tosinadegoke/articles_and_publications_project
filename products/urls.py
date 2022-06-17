from django.urls import path
from .views import (
    product_detail_view as pdv, 
    product_create_view as pcv,
    product_delete_view as pdelv,
    product_list_view as plv,
    product_update_view as puv,
)

# app_name = 'products'
urlpatterns = [
    path('details/<int:my_id>/', pdv, name='product_details'),
    # path('details/', pdv, name='product_details'),
    path('create/', pcv, name='create'),
    path('<int:prod_id>/delete', pdelv, name='product_delete'),
    path('<int:prod_id>/update', puv, name='product_update'),
    path('', plv, name='product_list'),     
]
