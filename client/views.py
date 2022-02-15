from django.http import HttpResponse
from .models import Client

# Create your views here.
from django.shortcuts import render


def listClient(request,pk):
    client = Client.objects.get(id=pk)
    commande = client.commande_set.all()
    comd_total = commande.count()
    context = {'client':client,'commande':commande,'comd_total':comd_total}
    return render(request,'client/listClient.html',context)