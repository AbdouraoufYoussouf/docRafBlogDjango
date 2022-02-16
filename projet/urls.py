
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('produit/',include('produit.urls')),
    path('client/',include('client.urls')),
    path('commande/',include('commande.urls')),
    path('',include('compte.urls')),
]
