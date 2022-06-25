"""djPractice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.urls.conf import include
from user.views import homepage_view, profile_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #   Create path for the Login and Logout system
    path('login/', auth_views.LoginView.as_view(template_name = 'user/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'user/logout.html'), name = 'logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name = 'user/password_reset.html'), name = 'password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = 'user/password_reset_done.html'), name = 'password_reset_done'),     # route to the page for succesful Password reset
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'user/password_reset_confirm.html'), name = 'password_reset_confirm'),     # route to the page for succesful Password reset
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'user/password_reset_complete.html'), name = 'password_reset_complete'),     # route to the page for succesful Password reset
    
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls')),
    path('pages/', include('my_page.urls')),
    path('products/', include('products.urls')),
    path('bookstore/', include('bookstore.urls')),
    path('Blog/', include('Blog.urls')),
    path('courses/', include('courses.urls')),
    path('user/', include('user.urls')),

    path('', homepage_view, name= 'index'),
    path('profile/', profile_view, name= 'profile'),
] 

if settings.DEBUG:      # if in Development mode
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    """
    1   - Submit email form                             PasswordResetView.as_view()
    2   - Email sent success message                    PasswordResetDoneView.as_view()
    1   - Link to password reset form in Email          PasswordResetConfirmView.as_view()
    1   - Password successfully changed message         PasswordResetcompleteView.as_view()
    """
