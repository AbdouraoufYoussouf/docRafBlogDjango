from .models import Client
from django.shortcuts import render
from commande.Filter import CommandeFilter

def listClient(request,pk):
    client = Client.objects.get(id=pk)
    commande = client.commande_set.all()
    comd_total = commande.count()
    myFilter = CommandeFilter(request.GET,queryset=commande)
    commande=myFilter.qs
    context = {'client':client,'commande':commande,'comd_total':comd_total,'myFilter':myFilter}
    return render(request,'client/listClient.html',context)