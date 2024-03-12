from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('logincheck/', views.logincheck, name='logincheck'),
    path('loginfbv/', views.loginfbv, name='loginfbv'),
    path('register/', views.register, name='register'),
    
]