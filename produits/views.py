from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.http import HttpResponse

from .models import Produit

# Create your views here.
def liste_produits(request):
	query = request.GET.get('q', '')
	produit_list = Produit.objects.all().order_by('date_peremption')
	if query:
		produit_list = produit_list.filter(nom__icontains=query)
	for produit in produit_list:
		print(f"{produit.nom} - date_peremption: {produit.date_peremption}")
	paginator = Paginator(produit_list, 5)

	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	return render(request, 'produits/liste_produits.html', {'page_obj': page_obj})

def add_produit(request):
	# This function is now renamed to post_produit
	return render(request, 'produits/add_produit.html')

def post_produit(request):

	if request.method == 'POST':
		nom = request.POST.get('nom')
		prix = request.POST.get('prix')
		date_peremption = request.POST.get('date_peremption')
		
		produit = Produit(nom=nom, prix=prix, date_peremption=date_peremption)
		produit.save()
		messages.success(request, "Produit ajouté avec succès !")
		return redirect('liste_produits')
	
	return redirect('add_produit')

def delete_produit(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)
    if request.method == 'POST':
        produit.delete()
        messages.success(request, "Produit supprimé avec succès !")
    return redirect('liste_produits')

def edit_produit(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)
    if request.method == 'POST':
        produit.nom = request.POST.get('nom')
        produit.prix = request.POST.get('prix')
        produit.date_peremption = request.POST.get('date_peremption')
        produit.save()
        return HttpResponse(status=200)
    return HttpResponse(status=400)