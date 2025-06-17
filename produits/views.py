from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Produit

# Create your views here.
def liste_produits(request):
	produit_list = Produit.objects.all().order_by('date_peremption')
	paginator = Paginator(produit_list, 5)

	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	print(page_obj)

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
		
		return redirect('liste_produits')
	
	return redirect('add_produit')