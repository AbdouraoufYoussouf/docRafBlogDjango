from django.http import HttpResponse
from django.shortcuts import redirect, render

from commande.forms import CommandeForm
from commande.models import Commande


def listcommande(request):
    return render(request,'commande/listCommande.html')

#*********** Ajouter une commande *********

def ajoutercommande(request):
    form = CommandeForm()
    if request.method == 'POST':
        form = CommandeForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/')
    titre = "Ajouter une commande"
    context = {'form': form,'titre':titre}
    return render(request,'commande/addCommande.html',context)

#*********** Modifier une commande *********

def modifiercommande(request,pk):
    commande = Commande.objects.get(id=pk)
    form = CommandeForm(instance=commande)
    if request.method == 'POST':
        form = CommandeForm(request.POST or None, instance=commande)
        if form.is_valid():
            form.save()
            return redirect('/')
    titre = "Modifier la commande"
    context = {'form': form,'titre':titre}
    return render(request,'commande/addCommande.html',context)

#*********** supprimer une commande *********

def supprimercommande(request,pk):
    commande = Commande.objects.get(id=pk)
    commande.delete()
    return redirect('home')
    



#*********** Autre façon def aire l'ajout *********

# def ajoutercommande(request):
#     form = CommandeForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('/')
#     context = {'form': form}
#     return render(request,'commande/addCommande.html',context)