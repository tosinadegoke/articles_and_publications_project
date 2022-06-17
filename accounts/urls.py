from re import template
from django.urls import path
from .import views
# from django.contrib.auth import views as auth_view
from django.contrib.auth.views import LoginView

app_name = 'accounts'
urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', auth_view.LoginView.as_view(template_name='account/login.html')),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
]
