from http import client
from telnetlib import STATUS
from django.db import models

class Commande(models.Model):
    STATUS=(('en instance', 'en instance'),
            ('non livré', 'non livré'),
            ('livré','livré'))
    # client = 
    # produit = 
    status = models.CharField(max_length=500,null=True,choices=STATUS)
    date_creation = models.DateTimeField(auto_now_add=True,null=True)
