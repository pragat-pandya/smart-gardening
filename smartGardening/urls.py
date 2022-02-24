from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('contact/', views.contact, name="contactUs"),
    path('user/', include('users.urls')),
    path('services/', include('services.urls')),
    path('aboutUs/', views.aboutUs, name='aboutUs'),
    path('terms&conditions/', views.terms, name='terms'),
]
