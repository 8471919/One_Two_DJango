from django.shortcuts import render

# Create your views here.
def landing(request):
    return render(
        request,
        'single_pages/index.html',
    )
    
def login(request):
    return render(
        request,
        'single_pages/login.html',
    )