from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pass

def vault_list(request):
    return render(request, 'vault/vault_list.html')

def add_password(request):
    if request.method == 'POST':
        site = request.POST.get('site')
        user = request.POST.get('username')
        newpass = request.POST.get('password')

        entry = Pass(username=user, site=site, password=newpass)
        entry.save()

        return HttpResponse("Account successfully added.")
    else:
        return HttpResponse("Invalid request method")