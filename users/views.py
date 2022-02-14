from django.shortcuts import render

# Create your views here.
def login(request):
    return render (request, 'users/login.html')

def user_profile (request):
    return render (request, 'users/profile.html')

def register (request):
    return render (request, 'users/register.html')
