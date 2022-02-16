from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listcommande),
    path('add_Commande', views.ajoutercommande,name='add_Commande'),
    path('edit_Commande/<str:pk>', views.modifiercommande,name='edit_Commande'),
    path('deletec/<pk>/', views.supprimercommande,name='deletec'),
]
