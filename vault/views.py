from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pass

def vault_list(request):
    entries_for_user = Pass.objects.filter(owner=request.user) #Updated and assisted by chatgpt on 12/3
    context = {
        "passwords": entries_for_user,
    }
    return render(request, 'vault/vault_list.html', context)

def add_password(request):
    if request.method == 'POST':
        site = request.POST.get('site')
        user = request.POST.get('username')
        newpass = request.POST.get('password')
        owner = request.user

        entry = Pass(owner=owner, username=user, site=site, password=newpass)
        entry.save()

        return redirect("vault")
    else:
        return HttpResponse("Invalid request method")