from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/write/', views.blog_create, name='blog_create'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('blog/edit/<int:pk>/', views.blog_update, name='blog_update'),
    path('blog/delete/<int:pk>/', views.blog_delete, name='blog_delete'),
    path('blog/search/<str:tag>/', views.blog_search, name='blog_search'),
]