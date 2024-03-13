from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls")),
    path("account/", include("account.urls")),
    path("blog/", views.post_list, name="post_list"),
    path("blog/<int:pk>/", views.post_detail, name="post_detail"),
    path("blog/write/", views.post_write, name="post_write"),
    path("blog/edit/<int:pk>/", views.post_edit, name="post_edit"),
    path("blog/delete/<int:pk>/", views.post_delete, name="post_delete"),
    path("blog/search/<str:tag>/", views.post_search, name="post_search"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)