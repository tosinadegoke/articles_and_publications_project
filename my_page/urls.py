from django.urls import path
from . import views

app_name = 'my_page'

urlpatterns = [
    path('', views.home_view),
    path('contact', views.contact_view),
    path('about', views.about_view),
]
