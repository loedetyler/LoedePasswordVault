from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# from django.http import HttpResponse

def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', { "form": form })

def loggedindash(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'dashboard.html')
    else:
        return render(request, 'invalid.html')