from django.db import models

class Produit(models.Model):
    nom = models.TextField(max_length=200,null=True)
    prix = models.FloatField(null=True)
