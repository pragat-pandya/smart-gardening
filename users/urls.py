from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('profile/', views.user_profile, name='user_profile'),
    path('register/', views.register, name='register')
]
