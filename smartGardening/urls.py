from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('contact-us/', views.contact, name="contactUs"),
    path('user/', include('users.urls')),
    path('services/', include('services.urls')),
    path('about-us/', views.aboutUs, name='aboutUs'),
    path('terms-and-conditions/', views.terms, name='terms'),
    path('privacy-policy/', views.privacy_policy, name='privacyPolicy'),
    path('tracker/', include('tracker.urls')),
    path('book-demo/', views.book_demo, name='bookDemo'),
]
