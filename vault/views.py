from django.shortcuts import render

def vault_list(request):
    return render(request, 'vault/vault_list.html')