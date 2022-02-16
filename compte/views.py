from importlib.resources import path
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login

from compte.forms import CreateUser

def logine(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,"username ou mot de passe incorrect")
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
