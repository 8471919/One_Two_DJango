from django.shortcuts import render, redirect


# Create your views here.
def landing(request):

    if(request.user.is_authenticated):
        return redirect('/diaries/')

    return render(
        request,
        'single_pages/index.html',
    )
    
def login(request):
    return render(
        request,
        'single_pages/login.html',
    )