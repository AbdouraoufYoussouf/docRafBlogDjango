from django.db import models
from django.forms import CharField

class Client(models.Model):
    nom = models.CharField(max_length=200,null=True)
    telephone = models.CharField(max_length=50,null=True)
    date_creation = models.DateTimeField(auto_now_add=True,null=True)