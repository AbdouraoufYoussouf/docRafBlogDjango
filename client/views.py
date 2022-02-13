from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render


def listClient(request):
    return render(request,'client/listClient.html')