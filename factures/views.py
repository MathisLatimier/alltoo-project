from django.shortcuts import render, redirect, get_object_or_404
from produits.models import Produit
from .models import Facture
from django.contrib import messages
from django.template.loader import render_to_string
from django.http import HttpResponse

def creer_facture(request):
    if request.method == 'POST':
        ids = request.POST.getlist('produits')
        produits = Produit.objects.filter(id__in=ids)
        facture = Facture.objects.create()
        facture.produits.set(produits)
        messages.success(request, f"Facture créée avec {produits.count()} produit(s) !")
        return redirect('liste_factures')
    query = request.GET.get('q', '')
    produits = Produit.objects.all()
    if query:
        produits = produits.filter(nom__icontains=query)
    return render(request, 'factures/creer_facture.html', {'produits': produits})

def liste_factures(request):
    factures = Facture.objects.all().order_by('-date')
    return render(request, 'factures/liste_factures.html', {'factures': factures})

def detail_facture(request, facture_id):
    facture = get_object_or_404(Facture, id=facture_id)
    total = sum([p.prix for p in facture.produits.all()])
    return render(request, 'factures/detail_facture.html', {'facture': facture, 'total': total})

