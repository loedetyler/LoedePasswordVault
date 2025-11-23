from django.shortcuts import render
# from django.http import HttpResponse

def homepage(request):
#    return HttpResponse("Hello, world. You've reached the vault.")
    return render(request, 'home.html')

def about(request):
#    return HttpResponse("This is the about page.")
    return render(request, 'about.html')

def login(request):
    return render(request, 'login.html')