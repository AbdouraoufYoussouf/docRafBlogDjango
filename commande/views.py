from django.http import HttpResponse
from django.shortcuts import redirect, render

from commande.forms import CommandeForm


def listcommande(request):
    return render(request,'commande/listCommande.html')

def ajoutercommande(request):
    form = CommandeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
   
    return render(request,'commande/addCommande.html',{'form': form})