from django.db import models
from produits.models import Produit

# Create your models here.

class Facture(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    produits = models.ManyToManyField(Produit, related_name='factures')

    def __str__(self):
        return f"Facture #{self.id} - {self.date.strftime('%Y-%m-%d %H:%M')}"
