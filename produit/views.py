from django.http import HttpResponse
from django.shortcuts import render

from commande.models import Commande
from client.models import Client

def home(request):
    commandes = Commande.objects.all()
    clients = Client.objects.all()
    context = {"clients":clients,"commandes":commandes}
    return render(request,'produit/acceuil.html',context)