from django.http import HttpResponse
from django.shortcuts import render


def listcommande(request):
    return render(request,'commande/listCommande.html')