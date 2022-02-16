from importlib.resources import path
from pyexpat.errors import messages
from django.shortcuts import render

from compte.forms import CreateUser

def login(request):
    return render(request,'compte/login.html')


def register(request):
    form = CreateUser()
    if request.method =='POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Compte creer avec succès pour mr '+ user)
    context = {'form':form}
    return render(request,'compte/register.html',context)
