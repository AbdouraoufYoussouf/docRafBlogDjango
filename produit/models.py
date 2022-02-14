from django.db import models

class Tag(models.Model):
    nom = models.CharField(max_length=200,null=True)

    def __str__(self) -> str:
        return self.nom

class Produit(models.Model):
    # idProd = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=200,null=True)
    prix = models.FloatField(null=True)
    tag = models.ManyToManyField(Tag)
    def __str__(self) -> str:
        return self.nom
