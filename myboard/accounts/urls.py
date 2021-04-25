from . import views
from django.contrib.auth import views as auth_views
from django.urls import path
urlpatterns = [
    # стандартныe обработчики Login, Logout
#    path('login/', views.UserLoginView.as_view(), name='login'),
#    path('logout/', views.UserLogOutView.as_view(), name='logout'),
#    path('register/', views.register, name='register'),
    path('profile/', views.UserProfile.as_view(), name='profile'),
]