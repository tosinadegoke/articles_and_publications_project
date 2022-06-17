from django.urls import path
from .views import (
    # f_bv,
    CourseView,
    CourseListView,
    MyListView,
    CourseCreateView,
    CourseUpdateView,
    CourseDeleteView
)

# app_name = 'courses'
urlpatterns = [
    # path('about/', f_bv, name = 'courses_about'),
    path('', CourseView.as_view(template_name = 'courses/about.html'), name = 'about'),
    path('<int:id>/', CourseView.as_view(), name = 'detail'),
    path('create/', CourseCreateView.as_view(), name = 'create'),
    path('list/', CourseListView.as_view(), name = 'list'),
    # path('list/', MyListView.as_view(), name = 'list'),
    path('<int:id>/update', CourseUpdateView.as_view(), name = 'update'),
    path('<int:id>/delete', CourseDeleteView.as_view(), name = 'delete'),
    
    
]
