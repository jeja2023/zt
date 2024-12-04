from django.urls import path
from login import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
]