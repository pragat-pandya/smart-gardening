from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def contact (request):
    return render(request, 'contactUs.html')

def aboutUs (request):
    return render (request, 'aboutUs.html')

def terms (request):
    return render (request, 'termsNConditions.html')

def privacy_policy(request):
    return render (request, 'privacy_policy.html')
